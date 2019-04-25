from functools import reduce
import test.zookeeper as zookeeper
from test.util import parse_boolean
import test.env as env

def api_global_url():
    return 'https://client-api.my-app.com/api' if env.prod() else 'https://client-api.tvoli.com/api'

def user_id():
    return '5JC8QBKHBMAW14W1ZBE8CXE9GUSR' if env.prod() else 'DQQ1O0YK89N9J99K302FRZUIGUSR'

def backend_secret():
    return config['BACKEND_SECRET_PROD'] if env.prod() else config['BACKEND_SECRET']

default_config = {
    'MAGINE_ENV': 'integration',
    'ZOOKEEPER_ADDRESS': env.zookeeper_address(),
    'API_GLOBAL_URL': api_global_url(),
    'EMAIL': 'api.test@my-app.com',
    'PASSWORD': 'api.test',
    'USER_ID': user_id(),
    'PARTNER_ID': 'my-app',
    'BACKEND_SECRET': 'put-api-backend-secret-from-vault-here',
    'BACKEND_SECRET_PROD': 'put-api-backend-secret-from-vault-here',
    'LOG_RESPONSE': '0' # whether to log http response bodies
}

def build_config(config, key):
    config[key] = env.env_value(key) or default_config[key]
    return config

config = reduce(build_config, default_config.keys(), {})

print('\nUsing config for env %s' % (env.env()))

def default_url(api_name):
    return zookeeper.server_urls(api_name)[0]

def url(api_name):
    key = api_name.upper().replace('-', '_') + '_URL'
    return config.get(key, None) or env.env_value(key) or default_url(api_name)

def credentials():
    return (config['EMAIL'], config['PASSWORD'], config['USER_ID'], config['PARTNER_ID'])

def boolean(key):
    return parse_boolean(config.get(key, None))
