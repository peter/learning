import json
from kazoo.client import KazooClient # pip install kazoo

import test.env as env

zk = KazooClient(hosts=env.zookeeper_address())
zk.start()

def service_path(service):
    return '/my-app/servers/%s' % service

def server_keys(service):
    return zk.get_children(service_path(service))

def server_path(service, server_key):
    return service_path(service) + '/' + server_key

def server_paths(service):
    return [server_path(service, key) for key in server_keys(service)]

def server_info(server_path):
    return json.loads(zk.get(server_path)[0].decode('utf-8'))

def server_url(server_path):
    endpoint = server_info(server_path)['serviceEndpoint']
    return 'http://%s:%s' % (endpoint['host'], endpoint['port'])

def server_urls(service):
    return [server_url(server_path(service, key)) for key in server_keys(service)]
