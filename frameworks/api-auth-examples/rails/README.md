# Ruby on Rails 5 API Authentation Example App

This is an example Rails API with JWT-based authentication and user registration.

## Dependencies

* Ruby 2
* Ruby on Rails 5
* PostgreSQL

## Install and Start Server

```
bundle install
bin/rails db:setup
bin/rails s
```

## Testing

Running unit tests:

```
bin/rails test
```

To run integration tests, first start the server:

```
bin/rails s
```

Then run the tests in a different terminal:

```
cd ..
pip install pytest
pip install requests
BASE_URL=http://localhost:3000 bin/test
```

## Deployment

There is a demo app running on Heroku, see example requests below.

## Example API Requests

For Heroku demo server:

```
export BASE_URL=https://api-auth-rails.herokuapp.com
```

For locally running server:

```
export BASE_URL=http://localhost:3000
```

Examples below with [httpie](https://httpie.org):

```
alias uuid="python -c 'import sys,uuid; sys.stdout.write(uuid.uuid4().hex)' | pbcopy && pbpaste && echo"
export EMAIL="admin-$(uuid)@example.com"

# Successful register (=> 201)
echo "{\"user\": {\"email\": \"$EMAIL\", \"password\": \"123\"}}" | http POST $BASE_URL/register

# Failed register (=> 422 (duplicate email))
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
rails new api-auth --database=postgresql --api
cd api-auth

bin/rails g model User name email password_digest recent_successful_logins:jsonb recent_failed_logins:jsonb
# Added to migration:
# null: false to email and password_digest columns
# add_index :users, [:email], :unique => true
bin/rails db:create
bin/rails db:migrate

# Add gem 'jwt' and gem 'bcrypt' to Gemfile
bundle install
# Add has_secure_password to user.rb (handles password encryption, limits password length to 72 characters)

bin/rails c
User.create!(email: 'admin@example.com' , password: '123')
User.find_by(email: 'admin@example.com')
exit

bin/rails db
select * from users;
\q

bin/rails g controller users register login me

# Modified routes in config/routes.rb
# post 'register', to: 'users/register'
# post 'login', to: 'users/login'
# get 'me', to: 'users/me'

# Added application code in these files:
# app/models/user.rb
# app/models/auth_token.rb
# config/initializers/auth_token.rb
# app/controllers/application_controller.rb
# app/controllers/users_controller.rb
```

## Resources

* [Token-based authentication with Ruby on Rails 5 API](https://www.pluralsight.com/guides/ruby-ruby-on-rails/token-based-authentication-with-ruby-on-rails-5-api)
* [Rails 5 Heroku Deployment](https://devcenter.heroku.com/articles/getting-started-with-rails5)
