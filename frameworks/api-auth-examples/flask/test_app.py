import app
import time

def test_get_request_jwt_claims():
    token = app.create_jwt_token(123)
    auth = 'Bearer %s' % token
    claims = app.get_request_jwt_claims({'Authorization': auth})
    assert claims['user_id'] == 123
    current_time = time.time()
    assert claims['exp'] > current_time
    assert claims['exp'] < (current_time + app.JWT_EXPIRY + 10)
