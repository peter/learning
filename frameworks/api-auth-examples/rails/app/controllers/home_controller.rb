class HomeController < ApplicationController
  skip_before_action :require_login, only: [:index]

  def index
    redirect_to '/swagger/index.html'
  end
end
