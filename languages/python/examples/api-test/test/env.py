import os

def env_value(key):
    return os.environ[key] if key in os.environ else None

def env():
    return env_value('MAGINE_ENV') or 'integration'

def prod():
    return env() == 'production'

def zookeeper_address():
    return 'zookeeper.service.com1_eu-west-1.consul:2181' if prod() else 'zookeeper.service.test-com_eu-west-1.consul:2181'
