import os
import re
import time
from datetime import datetime
from functools import wraps
from flask import g
from flask import Flask
from flask import send_from_directory
from flask import request, redirect
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from wtforms import Form, StringField, validators
from flask_bcrypt import Bcrypt
import jwt

app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)

SECRET_KEY = os.getenv('SECRET_KEY')
JWT_ALGORITHM = 'HS256'
JWT_EXPIRY = 24*3600

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

def create_jwt_token(user_id):
    exp = time.time() + JWT_EXPIRY
    claims = {'user_id': user_id, 'exp': exp}
    return str(jwt.encode(claims, SECRET_KEY, algorithm=JWT_ALGORITHM), 'utf-8')

def get_request_jwt_claims(headers):
    try:
        header_match = re.search('^Bearer (.+)$', headers.get('Authorization', ''))
        token = header_match and header_match.group(1)
        return token and jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
    except Exception as error:
        print('get_request_jwt_claims error=%s' % error)
        return None

def create_login_attempt(user, success):
    db.session.add(LoginAttempt(user_id=user.id, login_at=datetime.now(), success=success))
    db.session.commit()

def create_user(attributes):
    user = User(**attributes)
    db.session.add(user)
    db.session.commit()
    return user

def get_request_user(headers):
    claims = get_request_jwt_claims(headers)
    return claims and User.query.get(claims['user_id'])

def require_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        g.current_user = get_request_user(request.headers)
        if not g.current_user:
            return (jsonify({'error': 'login required'}), 401)
        return f(*args, **kwargs)
    return decorated_function

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_digest = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_digest = str(bcrypt.generate_password_hash(password), 'utf-8')

    def verify_password(self, password):
        return password and bcrypt.check_password_hash(self.password_digest, password)

    def recent_successful_logins(self):
        query = (LoginAttempt.query
                    .filter_by(user_id=self.id, success=True)
                    .order_by(LoginAttempt.login_at.desc())
                    .limit(5))
        return [{'time': a.login_at} for a in query.all()]

    def public_attributes(self):
        return {'name': self.name, 'email': self.email, 'recent_successful_logins': self.recent_successful_logins()}

    def __repr__(self):
        return '<User %r>' % self.email

class UserForm(Form):
    email = StringField('Email', [validators.Required(), validators.Length(min=3, max=80), validators.Email('must be valid email')])
    password = StringField('Password', [validators.Required(), validators.Length(min=3, max=80)])
    name = StringField('Name', [validators.Optional(), validators.Length(min=3, max=80)])

class LoginAttempt(db.Model):
    __tablename__ = 'login_attempts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    login_at = db.Column(db.DateTime, nullable=False)
    success = db.Column(db.Boolean, nullable=False)

    def public_attributes(self):
        return {'user_id': self.user_id, 'login_at': self.login_at, 'success': self.success}

    def __repr__(self):
        return '<LoginAttempt user_id=%s login_at=%s success=%s>' % (self.user_id, self.login_at, self.success)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/')
def redirect_to_swagger():
    return redirect('static/swagger/index.html')

@app.route('/register', methods=['POST'])
def register():
    attributes = request.get_json().get('user', {})
    form = UserForm(**attributes)
    if form.validate():
        user = create_user(attributes)
        return (jsonify({'user': user.public_attributes()}), 201)
    else:
        return (jsonify({'errors': form.errors}), 422)

@app.route('/login', methods=['POST'])
def login():
    params = request.get_json()
    user = User.query.filter_by(email=params['email']).first()
    success = user and user.verify_password(params['password'])
    if user:
        create_login_attempt(user, success)
    if success:
        return jsonify({
            'token': create_jwt_token(user.id),
            'user': user.public_attributes()})
    else:
        return (jsonify({'error': 'invalid credentials'}), 401)

@app.route('/me')
@require_login
def me():
    return jsonify({'user': g.current_user.public_attributes()})
