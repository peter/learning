require 'test_helper'

class UserTest < ActiveSupport::TestCase
  test "create/authenticate" do
    attributes = {email: 'admin@example.com' , password: '123'}
    User.create!(attributes)
    user = User.find_by(email: attributes[:email])
    assert_equal attributes[:email], user.email
    assert user.authenticate(attributes[:password])
  end
end
