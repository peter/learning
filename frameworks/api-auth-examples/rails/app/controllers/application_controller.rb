class ApplicationController < ActionController::API
  before_action :require_login

  private

  def require_login
    token = AuthToken.from_headers(request.headers)
    token_payload = token && AuthToken.decode(token)
    @current_user = token_payload && User.find(token_payload['user_id'])
    render(json: {error: 'Not Authorized'}, status: 401) unless @current_user
  end
end
