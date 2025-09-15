# Clickhouse

Query billions of rows in milliseconds

## Introduction

Clickhouse is:

* An OLAP database rather than an OLTP database. OLAP databases are optimized for analytical queries, not for transactional updates. Analytics is fundamentally about answering questions and providing insights.
* Column oriented rather than Row oriented. Every column is stored in its own optimized/compressed binary file
* Highly optimized in terms of query response time, i.e. it's up to 1000x faster than a traditional OLTP database
* Able to utilize all available cores, all available memory, and multiple servers
* A database that enables real time analytics of logs and events, typically ingested via Kafka
* Open Source
* Able to run on your laptop or your own server or as a managed service
* Used by Posthog, Sentry, Disney+, Cloudflare, Ebay, Uber etc.
* Compliant with ANSI SQL column data types and those are aliases to the internal data types that Clickhouse uses
* Clickhouse is implemented in C++

You can evaluate Clickhouse cloud for free during a 30 day trial period (with 300 USD credits)

## Running Clickhouse locally

```sh
# Starting the clickhouse server:
clickhouse server

# Connecting to the server (on port 9000)
clickhouse client
SHOW TABLES;
SHOW TABLES FROM system;
DESCRIBE TABLE my_table;
SHOW CREATE TABLE my_table;
```

## Resources

* [Clickhouse Getting Started](https://clickhouse.com/docs/getting-started/quick-start/oss)
* [Clickhouse Mac Install](https://clickhouse.com/docs/install/macOS)
* [Clickhouse Docs](https://clickhouse.com/docs)
* [Clickhouse Learning](https://learn.clickhouse.com)
* [Clickhouse Query Optimization Workshop September 2025 (Pablo Musa)](https://learn.clickhouse.com/visitor_catalog_class/show/1786439)
* [Clickhouse Cloud](https://console.clickhouse.cloud)
* [Clickhouse Realtime Modeling of Weather Data Case Stury](https://www.ssp.sh/blog/practical-data-modeling-clickhouse/)

* [ClickStack/HyperDX - Clickhouse Observability Platform](https://www.hyperdx.io) ([Clickhouse/HyperDX acquisition](https://clickhouse.com/blog/clickhouse-acquires-hyperdx-the-future-of-open-source-observability))

Other open source analytics databases:

* [DuckDB](https://duckdb.org)
* [StarRocks - Clickhouse alternative](https://github.com/StarRocks/StarRocks)
* [Clickhouse / StarRocks Comparison](https://www.starrocks.io/blog/starrocks-vs-clickhouse-the-quest-for-analytical-database-performance)
* [ClickBench - Performance Benchmark for Analytical DBMS](https://benchmark.clickhouse.com)
