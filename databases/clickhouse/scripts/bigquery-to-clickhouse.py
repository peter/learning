#! /usr/bin/env python3

# USAGE:
#
# DATE_PARTITION=2025-09-09 bigquery-to-clickhouse.py | jq

import json
import logging
import os
import sys
import time
from datetime import datetime, timedelta

# pip3 install pandas
# pip3 install db-dtypes
import pandas as pd

# https://cloud.google.com/python/docs/reference/bigquery/latest
# pip3 install google-cloud-bigquery
# pip3 install google-cloud-bigquery-storage
from google.cloud import bigquery

# https://clickhouse.com/docs/integrations/python
# pip3 install clickhouse-connect
import clickhouse_connect

BQ_TABLE_NAME = os.getenv("BQ_TABLE_NAME")
CLICKHOUSE_TABLE_NAME = os.getenv("CLICKHOUSE_TABLE_NAME")


def get_yesterday_date() -> str:
    yesterday = datetime.now() - timedelta(days=1)
    return yesterday.strftime("%Y-%m-%d")


# Configure JSON logging to stdout
class JsonLogFormatter(logging.Formatter):
    def format(self, record):
        log_obj = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if hasattr(record, "args"):
            log_obj["args"] = record.args
        return json.dumps(log_obj)


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonLogFormatter())
    logger.addHandler(handler)
    return logger


logger = get_logger()


def bigquery_query(date_partition: str) -> pd.DataFrame:
    # bigquery_client = bigquery.Client()
    service_account_path = os.getenv(
        "BIGQUERY_SERVICE_ACCOUNT_PATH",
        "/Users/petermarklund/notes/bigquery-service-account-key-attention-score-api.json",
    )
    bigquery_client = bigquery.Client.from_service_account_json(service_account_path)
    elapsed_start = time.time()
    BQ_SQL = f"""
        SELECT *
        FROM `{BQ_TABLE_NAME}`
        WHERE date_partition = "{date_partition}"
    """
    query_job = bigquery_client.query(BQ_SQL)
    result = query_job.result()
    elapsed = time.time() - elapsed_start
    logger.info(
        f"bigquery_query finished",
        {
            "elapsed": elapsed,
            "n_rows": result.total_rows,
            "date_partition": date_partition,
            "sql": BQ_SQL,
        },
    )
    return result.to_dataframe()


def get_clickhouse_client():
    clickhouse_host = os.getenv(
        "CLICKHOUSE_HOST", "u2a4rcb0v3.eu-west-1.aws.clickhouse.cloud"
    )
    clickhouse_password = os.getenv("CLICKHOUSE_PASSWORD")
    client = clickhouse_connect.get_client(
        host=clickhouse_host,
        port=8443,
        username="default",
        password=clickhouse_password,
        secure=True,
        verify=False,  # Disable SSL verification - use with caution
    )
    return client


def clickhouse_insert(client, date_partition: str, df: pd.DataFrame):
    if df.empty:
        logger.warning("data frame empty - skipping clickhouse insert")
        return

    data = df.to_dict("records")
    total_rows = len(data)
    logger.info("Inserting into ClickHouse table", {"total_rows": total_rows})

    column_names = list(data[0].keys())
    values = [tuple(row[col] for col in column_names) for row in data]
    elapsed_start = time.time()
    count_before = clickhouse_count(client)
    # NOTE: seems a delete is not needed?
    # client.query(f"delete from {CLICKHOUSE_TABLE_NAME} where date_partition = '{date_partition}'")
    result = client.insert(CLICKHOUSE_TABLE_NAME, values, column_names=column_names)
    elapsed = time.time() - elapsed_start
    count_after = clickhouse_count(client)
    logger.info(
        "Clickhouse insert finished",
        {
            "result": vars(result),
            "elapsed": elapsed,
            "count_before": count_before,
            "count_after": count_after,
            "date_partition": date_partition,
        },
    )
    return result


def clickhouse_query(client, sql):
    return client.query(sql)


def clickhouse_count(client):
    result = clickhouse_query(client, f"select count(*) from {CLICKHOUSE_TABLE_NAME}")
    return result.result_rows[0][0]


def main():
    date_partition = os.getenv("DATE_PARTITION")
    if date_partition is None:
        date_partition = get_yesterday_date()
    logger.info("script starting", {"date_partition": date_partition})

    df = bigquery_query(date_partition)

    client = get_clickhouse_client()
    clickhouse_insert(client, date_partition, df)


if __name__ == "__main__":
    main()
