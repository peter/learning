import sys
import os
import json
import psycopg2
import psycopg2.extras

def require_python3():
    if sys.version_info[0] < 3:
        print('Sorry, this script requires Python 3, please upgrade')
        sys.exit(1)

require_python3()

def env(key, default=None):
    return os.environ[key] if key in os.environ else default

SCHEMA_NAME = env('DATABASE_SCHEMA', 'foobar')
TABLES_QUERY = f'select distinct schemaname, tablename from pg_table_def where schemaname = \'{SCHEMA_NAME}\''

DB_CONFIG_DEFAULTS = {
    'database': env('DATABASE', ''),
    'user': env('DATABASE_USER', ''),
    'password': env('DATABASE_PASSWORD'),
    'port': env('DATABASE_PORT', '5439')
}

DATE_COLUMNS = {
    'view.foobar': 'foobar'
}

def difference(list1, list2):
    set2 = set(list2)
    return [item for item in list1 if item not in set2]

def intersection(list1, list2):
    set2 = set(list2)
    return [item for item in list1 if item in set2]

def combined_diff(list1, list2):
  removed = difference(list1, list2),
  added = difference(list2, list1)
  return {'removed': removed, 'added': added} if (len(removed) > 0 or len(added) > 0) else None

def pretty_json(value):
    return json.dumps(value, indent=4, sort_keys=True)

def get_conn(db_config):
    return psycopg2.connect(**db_config)

def query_tuple(conn, *args):
    cur = conn.cursor()
    cur.execute(*args)
    return cur.fetchall()

def query_dict(conn, *args):
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(*args)
    return map(dict, cur.fetchall())

def query_values(conn, *args):
    result = query_tuple(conn, *args)
    return list(map(lambda r: r[0], result))

def query_value(conn, *args):
    result = query_values(conn, *args)
    return result and result[0]

def count(conn, table, where_clause=None):
    where_string = f' where {where_clause}' if where_clause else ''
    query = f'select count(1) from {table}{where_string}'
    return query_value(conn, query)

def date_list(conn, table, date_column, max_date):
  query = f'select distinct TRUNC({date_column}) from {table} where {date_column} < \'{max_date}\' order by {date_column} desc'
  return list(map(str, query_values(conn, query)))

def column_types(conn, table):
  schemaname, tablename = table.split('.')
  query = f'select "column", type from PG_TABLE_DEF where schemaname = \'{schemaname}\' and tablename = \'{tablename}\''
  return query_dict(conn, query)

def is_date_type(column_type):
  return 'timestamp' in column_type or column_type == 'date'

def date_columns(conn, table):
  return [t['column'] for t in column_types(conn, table) if is_date_type(t['type'])]

def first(l):
  return None if not l else l[0]

def qualified_table(table):
    return '.'.join([table['schemaname'], table['tablename']])

def merge(dict1, dict2):
    return {**dict1, **dict2}

def get_table_names(conn):
    return list(map(qualified_table, query_dict(conn, TABLES_QUERY)))

def main():
    max_date = env('MAX_DATE', '2018-08-01')
    conn1 = get_conn(merge(DB_CONFIG_DEFAULTS, {
        'host': env('DATABASE_HOST1', 'foobar.eu-west-1.redshift.amazonaws.com')
    }))
    conn2 = get_conn(merge(DB_CONFIG_DEFAULTS, {
        'host': env('DATABASE_HOST2', 'foobar.eu-west-1.redshift.amazonaws.com')
    }))
    print(f'Database conn1: {conn1}')
    print(f'Database conn2: {conn2}')

    tables1 = get_table_names(conn1)
    tables2 = get_table_names(conn2)
    removed_tables = difference(tables1, tables2)
    added_tables = difference(tables2, tables1)
    common_tables = intersection(tables1, tables2)

    # print(f'DEBUG Tables 1: {tables1}')
    # print(f'DEBUG Tables 2: {tables2}')
    print(f'Tables 1 count: {len(tables1)}')
    print(f'Tables 2 count: {len(tables2)}')
    print(f'Removed tables: {removed_tables}')
    print(f'Added tables: {added_tables}')

    diffs = []
    diff_tables_count = 0
    for table in common_tables:
        date_column = DATE_COLUMNS.get(table, first(date_columns(conn1, table)))
        date_clause = f'{date_column} < \'{max_date}\'' if date_column else None
        count1 = count(conn1, table, date_clause)
        count2 = count(conn2, table, date_clause)
        date_list1 = date_list(conn1, table, date_column, max_date) if date_column else None
        date_list2 = date_list(conn2, table, date_column, max_date) if date_column else None
        date_difference = combined_diff(date_list1, date_list2) if date_column else 'unknown'
        diff = count2 - count1
        diff_percent = round(diff/count1*100, 3) if count1 > 0 else None
        if diff != 0:
            diff_tables_count += 1
            diffs.append({'table': table, 'date_column': date_column, 'count1': count1, 'count2': count2, 'diff': diff, 'diff_percent': diff_percent, 'date_difference': date_difference})
            print(f'table: {table}, date_column: {date_column}, count1: {count1}, count2: {count2}, diff: {diff}, diff_percent: {diff_percent}, date_difference: {date_difference}')

    sorted_diffs = sorted(diffs, key=lambda d: abs(d['diff_percent']), reverse=True)

    print(f'Out of {len(common_tables)} tables {diff_tables_count} tables had different counts')

    print('\nSORTED DIFFS:\n')

    print(pretty_json(sorted_diffs))

if __name__ == '__main__':
    main()
