import test.http_client as http_client
import test.config as config
from test.type_spec import typeSpec, type_check, Dict
from requests.models import Response

VERSION = 'v2'

def Partner(v):
    return type_check(v, {
        'id': str,
        'backendSecret': str
    })

def User(v):
    return type_check(v, {
        'userId': str,
        'token': str
    })

@typeSpec(Partner, User, dict)
def headers(partner, user):
    return {
        'MyApp-PartnerId': partner['id'],
        'MyApp-PartnerBackendSecret': partner['backendSecret'],
        'Authorization': f'Bearer {user["token"]}'
    }

@typeSpec(str, str)
def api_url(path):
    return f'{config.url("billing")}/billing/{VERSION}{path}'

@typeSpec(Partner, User, Response)
def get_payment_method(partner, user):
    url = api_url(f'/users/{user["userId"]}/payment_method')
    return http_client.get(url, headers=headers(partner, user))

@typeSpec(Partner, User, Response)
def get_payments(partner, user):
    url = api_url(f'/users/{user["userId"]}/payments')
    return http_client.get(url, headers=headers(partner, user))
