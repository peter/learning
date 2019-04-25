import test.http_client as http_client
import test.config as config

def login_url():
    return '%s/login/v2/auth/email' % (config.url('api_global'))

def dynamic_url(user_id):
    return '%s/user/v2/users/%s/dynamic' % (config.url('api_global'), user_id)

def login(client_api_token, email, password):
    headers = {'MyApp-AccessToken': client_api_token}
    data = {'identity': email, 'accessKey': password}
    return http_client.post(login_url(), data, headers)

def get_dynamic(user_id, client_api_token, user_token):
    authorization = 'Bearer %s' % (user_token)
    headers = {'MyApp-AccessToken': client_api_token, 'Authorization': authorization}
    return http_client.get(dynamic_url(user_id), headers=headers).json()

def set_dynamic(user_id, client_api_token, user_token, data):
    authorization = 'Bearer %s' % (user_token)
    headers = {'MyApp-AccessToken': client_api_token, 'Authorization': authorization}
    return http_client.put(dynamic_url(user_id), data, headers)
