class User < ApplicationRecord
  EMAIL_PATTERN = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]{2,})\z/i
  RECENT_LOGINS_LIMIT = 5
  has_secure_password
  validates :email, uniqueness: true, format: {with: EMAIL_PATTERN, on: :create}

  def auth_token
    AuthToken.encode({user_id: id})
  end

  def save_recent_login!(success)
    login = {time: Time.zone.now}
    attribute = success ? :recent_successful_logins : :recent_failed_logins
    self.send("#{attribute}=", ([login] + (self.send(attribute) || [])).first(RECENT_LOGINS_LIMIT))
    save!
  end

  def public_attributes
    attributes.slice('name', 'email', 'recent_successful_logins', 'recent_failed_logins')
  end
end
