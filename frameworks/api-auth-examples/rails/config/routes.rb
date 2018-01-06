Rails.application.routes.draw do
  root to: 'home#index'

  post 'register', to: 'users#register'
  post 'login', to: 'users#login'
  get 'me', to: 'users#me'
end
