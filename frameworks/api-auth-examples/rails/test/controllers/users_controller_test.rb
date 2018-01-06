require 'test_helper'

class UsersControllerTest < ActionDispatch::IntegrationTest
  setup do
    AuthToken.default_secret = Rails.application.secrets.secret_key_base
    @user = User.create!(user_attributes)
  end

  test "register" do
    post register_url, params: {user: user_attributes}
    assert_response :success
  end

  test "login" do
    post login_url, params: {email: @user.email, password: @user.password}
    assert_response :success
    token = JSON.parse(response.body)['token']
    assert token.present?
    assert_equal @user.id, AuthToken.decode(token)['user_id']
  end

  test "me" do
    token = @user.auth_token
    get me_url, headers: {Authorization: "Bearer #{token}"}
    assert_response :success
  end

  def user_attributes
    {email: "test-user-#{SecureRandom.uuid}@example.com", password: '123'}
  end
end
