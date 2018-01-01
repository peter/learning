# Python/Flask REST API Example

## Invoking the API

```
export BASE_URL=http://localhost:5000
export AUTH=miguel:python

# list
curl -i -u $AUTH $BASE_URL/v1/tasks

# get
curl -i -u $AUTH $BASE_URL/v1/tasks/1

# create
curl -i -u $AUTH -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' $BASE_URL/v1/tasks

# update
curl -i -u $AUTH -H "Content-Type: application/json" -X PUT -d '{"done":true}' $BASE_URL/v1/tasks/2

# delete
curl -i -u $AUTH -X DELETE $BASE_URL/v1/tasks/2
```

## Talking to Postgres

```
createdb python-rest-api
psql python-rest-api < data.sql
python
import db
conn = db.conn('postgresql://postgres:@localhost/python-rest-api')

# list
db.query(conn, "select * from items")

# create
db.execute(conn, 'INSERT INTO items ("title", "body") VALUES (%s, %s)', ("Hello World", "This is the body"))

# get
db.query_one(conn, "select * from items where id = 1")

# update
db.execute(conn, 'UPDATE items SET title = %s where id = %s', ("Hello World!", 1))

# delete
db.execute(conn, 'DELETE from items where id = %s', ([1]))
```

## Resources

* [Flask REST example](https://gist.github.com/miguelgrinberg/5614326)
