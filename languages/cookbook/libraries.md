# Library Dependencies

## Managing Versions of Libraries

Python:

```bash
# Create virtual env
pip install virtualenv
virtualenv venv
. venv/bin/activate

# Install libraries and put them in requirements.txt
pip install Flask psycopg2 Flask-SQLAlchemy Flask-Migrate Flask-Bcrypt PyJWT WTForms
pip freeze > requirements.txt

# Installing libraries with versions in requirements.txt
pip install -r requirements.txt
```
