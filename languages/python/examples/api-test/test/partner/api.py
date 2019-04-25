import test.http_client as http_client
import test.config as config

def get_url(partner_id):
    return '%s/partner/v2/partner/%s' % (config.url('partner'), partner_id)

def get(partner_id):
    return http_client.get(get_url(partner_id))
