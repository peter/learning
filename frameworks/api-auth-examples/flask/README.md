# Flask API Authentation Example App

## Dependencies

* Python 3
* PostgreSQL
* Flask

## Installing and Starting the Server

```
pip install virtualenv
. venv/bin/activate

pip install -r requirements.txt

createdb api-auth-flask-dev

python
from app import db
db.create_all()
```

Start dev server:

```
/bin/start-dev
```

## Testing

Running unit tests:

```
. venv/bin/activate
pip install pytest
bin/test
```

To run integration tests, first start the server:

```
bin/start-dev
```

Then run the tests in a different terminal:

```
deactivate
cd ..
pip install pytest
pip install requests
BASE_URL=http://localhost:5000 bin/test
```

## Example API Requests

For locally running server:

```
export BASE_URL=http://localhost:5000
```

For Heroku demo app:

```
export BASE_URL=http://api-auth-flask.herokuapp.com
```

Examples below with [httpie](https://httpie.org):

```
alias uuid="python -c 'import sys,uuid; sys.stdout.write(uuid.uuid4().hex)' | pbcopy && pbpaste && echo"
export EMAIL="admin-$(uuid)@example.com"

# Successful register (=> 201)
echo "{\"user\": {\"email\": \"$EMAIL\", \"password\": \"123\"}}" | http POST $BASE_URL/register

# Successful login (=> 200, returns token)
echo "{\"email\": \"$EMAIL\", \"password\": \"123\"}" | http POST $BASE_URL/login
export TOKEN=<token-in-response-above>

# Failed login attempt (=> 401)
echo "{\"email\": \"$EMAIL\", \"password\": \"122\"}" | http POST $BASE_URL/login

# Successful get user info (=> 200, returns recent_successful_logins)
http $BASE_URL/me Authorization:"Bearer $TOKEN"

# Failed get user info (=> 401)
http $BASE_URL/me
```

## How this App was Created

```
pip install virtualenv
mkdir flask
cd flask

virtualenv venv
. venv/bin/activate

pip install Flask psycopg2 Flask-SQLAlchemy Flask-Migrate Flask-Bcrypt PyJWT WTForms
pip freeze > requirements.txt

createdb api-auth-flask-dev

python
from app import db
db.create_all()
from app import User
from app import bcrypt
# password_digest = bcrypt.generate_password_hash('123')
user = User(email='admin@example.com', password='123')
db.session.add(user)
db.session.commit()

psql api-auth-flask-dev
select * from users;
```

## TODO

* Double register of user yields 500 (db error)
* pyflakes

## AWS Lambda Deployment

Setting up deployment with [Zappa](https://github.com/Miserlou/Zappa):

```
pip install zappa
zappa init
zappa deploy dev
# https://qcaffbx4w7.execute-api.eu-central-1.amazonaws.com/dev
# To get resources to work: On the API Gateway dashboard choose Resources, click Actions and choose Deploy API
# Added DATABASE_URL and SECRET_KEY env variables in AWS console UI
```

NOTE: The root path is /dev and not /. It may be [this cannot be fixed](https://stackoverflow.com/questions/42306810/rewriterules-for-aws-lambda-and-aws-api-gateway) without
a custom domain.

```
export BASE_URL=https://qcaffbx4w7.execute-api.eu-central-1.amazonaws.com/dev
```

Various useful Zappa commands:

```
zappa status dev
zappa tail dev
zappa tail dev --http --filter "POST"
zappa invoke production 'app.my_function'
```

To deploy:

```
zappa update dev
```

## Heroku Deployment

There is a [demo Heroku deployment](http://api-auth-flask.herokuapp.com) available.

How Heroku deployment was set up:

```
pip install gunicorn
pip freeze > requirements.txt
echo "web gunicorn app:app" > Procfile

heroku apps:create api-auth-flask
heroku addons:create heroku-postgresql:hobby-dev -a api-auth-flask

cd ..
heroku git:remote -a api-auth-flask
heroku git:remote -a api-auth-flask
git subtree push --prefix flask heroku master

heroku run python -a api-auth-flask
from app import db
db.create_all()
exit()

heroku logs --tail -a api-auth-flask
```

## NOTES

* No way to protect all routes by default in Flask (https://stackoverflow.com/questions/31368633/how-do-i-make-sure-a-flask-app-has-been-authorized-on-all-routes)

## Resources

* [Token-Based Authentication With Flask](https://realpython.com/blog/python/token-based-authentication-with-flask)
* [Securing REST APIs: Basic HTTP Authentication with Python / Flask](http://polyglot.ninja/securing-rest-apis-basic-http-authentication-python-flask)

* [Flask by Example - Setting Up Postgres, SQLAlchemy, and Alembic](https://realpython.com/blog/python/flask-by-example-part-2-postgres-sqlalchemy-and-alembic)

* [Build a CRUD Web App With Python and Flask](https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one)

* [PyJWT](http://pyjwt.readthedocs.io/en/latest)

* [Flask-SQLAlchemy (ORM)](http://flask-sqlalchemy.pocoo.org/2.3)
* [Flask-Migrate](https://github.com/miguelgrinberg/Flask-Migrate)
* [Flask-Bcrypt](http://flask-bcrypt.readthedocs.io/en/0.7.1)

* [Flask (Web Framework)](http://flask.pocoo.org)
* [Flask Documentation (PDF)](http://flask.pocoo.org/docs/0.12/.latex/Flask.pdf)

* [Zappa/AWS Lambda (Deployment)](https://github.com/Miserlou/Zappa)
* [Update Amazon RDS max_connections with Parameter](https://github.com/jollygoodcode/jollygoodcode.github.io/issues/16)

* [Hug (Python API Framework)](http://www.hug.rest)
* [Zappa Hug Example (Hug/Lambda Deployment)](https://github.com/mcrowson/zappa-hug-example)
