import test.http_client as http_client
import test.config as config

def get_subscription(user_id, client_api_token, user_token):
    url = '%s/superscription/v2/users/%s/subscription' % (config.url('api_global'), user_id)
    authorization = 'Bearer %s' % (user_token)
    headers = {'MyApp-AccessToken': client_api_token, 'Authorization': authorization}
    return http_client.get(url, headers=headers)
