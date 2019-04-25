import test.http_client as http_client
import test.config as config
from test.type_spec import typeSpec
from requests.models import Response

@typeSpec(str, dict)
def headers(partner_id):
    authorization = 'Bearer internal:{}'.format(config.backend_secret())
    return {'MyApp-PartnerId': partner_id, 'Authorization': authorization}

@typeSpec(str, str)
def api_url(path):
    base_url = config.url('nibble')
    return f'{base_url}/nibble/v1{path}'

@typeSpec(str, str, Response)
def query(partner_id, query):
    url = api_url(f'/query?q={query}&size=-1')
    return http_client.get(url, headers=headers(partner_id))
