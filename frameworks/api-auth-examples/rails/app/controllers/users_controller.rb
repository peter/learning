class UsersController < ApplicationController
  skip_before_action :require_login, only: [:register, :login]

  def register
    @user = User.new(user_params)
    if @user.save
      render json: {user: @user.public_attributes}, status: :created
    else
      render json: @user.errors, status: :unprocessable_entity
    end
  end

  def login
    user = User.find_by(email: params[:email])
    success = (user && user.authenticate(params[:password])).present?
    user.save_recent_login!(success) if user
    if user && success
      render json: {token: user.auth_token}
    else
      render json: {error: 'invalid credentials'}, status: :unauthorized
    end
  end

  def me
    render json: {user: @current_user.public_attributes}
  end

  private

  def user_params
    params.require(:user).permit(:name, :email, :password)
  end
end
