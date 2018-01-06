module AuthToken
  @default_expiry = 24.hours # duration until expiry
  class << self
    attr_accessor :default_secret, :default_expiry
  end

  def self.from_headers(headers)
    headers['Authorization'] && headers['Authorization'][/^Bearer (.+)$/, 1]
  rescue
    nil
  end

  def self.decode(token, secret = default_secret)
    JWT.decode(token, secret)[0]
  rescue
    nil
  end

  def self.encode(payload, expiry = default_expiry, secret = default_secret)
    payload[:exp] = expiry.from_now.to_i
    JWT.encode(payload, secret)
  end
end
