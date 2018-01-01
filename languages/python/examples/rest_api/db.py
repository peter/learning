# -*- coding: UTF-8 -*-

import sys
import psycopg2

reload(sys)
sys.setdefaultencoding('utf-8')

def conn(db_config):
    print("Connecting to database %s" % (db_config))
    conn = psycopg2.connect(db_config)
    conn.autocommit = True
    return conn

def execute(conn, *args):
    cur = conn.cursor()
    cur.execute(*args)

def query(conn, *args):
    cur = conn.cursor()
    cur.execute(*args)
    return cur.fetchall()

def query_one(conn, *args):
    return query(conn, *args)[0]

def query_values(conn, *args):
    result = query(conn, *args)
    return map(lambda r: r[0], result)

def query_value(conn, *args):
    result = query_values(conn, *args)
    return result and result[0]
