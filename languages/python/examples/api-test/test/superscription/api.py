import test.config as config
import test.http_client as http_client

def headers(partner_id):
    authorization = 'Bearer internal:%s' % (config.backend_secret())
    return {'MyApp-PartnerId': partner_id, 'Authorization': authorization}

def url(user_id, sub_path='', version='v2'):
    return '%s/superscription/%s/users/%s/subscription%s' % (config.url('superscription'), version, user_id, sub_path)

def get_subscription(user_id, partner_id):
    return http_client.get(url(user_id), headers=headers(partner_id))

def get_history(user_id, partner_id):
    return http_client.get(url(user_id, '/history'), headers=headers(partner_id))

def add(user_id, partner_id, data):
    return http_client.put(url(user_id, '/add'), data, headers=headers(partner_id))

def cancel(user_id, partner_id, data):
    return http_client.put(url(user_id, '/cancel'), data, headers=headers(partner_id))
