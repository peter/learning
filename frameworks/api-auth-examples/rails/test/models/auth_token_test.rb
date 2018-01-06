require 'test_helper'

class AuthTokenTest < ActiveSupport::TestCase
  setup do
    AuthToken.default_secret = Rails.application.secrets.secret_key_base
  end

  test "from_headers - extracts JWT token from headers" do
    token = SecureRandom.uuid
    assert_equal token, AuthToken.from_headers({'Authorization' => "Bearer #{token}"})
    assert_nil AuthToken.from_headers({'Authorization' => "foobar"})
    assert_nil AuthToken.from_headers({})
  end

  test "encode/decode - we can create/parse JWT token with claims hash and expiry" do
    assert AuthToken.default_secret
    claims = AuthToken.decode(AuthToken.encode({user_id: 123}))
    assert_equal(claims['user_id'], 123)
    assert AuthToken.default_expiry > 3600
    assert claims['exp'] <= AuthToken.default_expiry.from_now.to_i
    assert claims['exp'] >= (AuthToken.default_expiry.from_now.to_i - 10)

    assert_nil AuthToken.decode('foobar')
  end
end
