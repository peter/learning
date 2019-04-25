import pytest
import test.billing.api as api
import test.partner.api as partner_api
import test.user.api as user_api
from test.assert_helper import assert_equal
from test.util import deep_get
import test.config as config

PARTNER_ID = 'my-app'
context = {}

def test_setup():
    email, password, user_id, partner_id = config.credentials()
    context['partner'] = partner_api.get(PARTNER_ID).json()
    context['user'] = user_api.login(context['partner']['clientApiToken'], email, password).json()
    print(f'user={context["user"]}')

def test_get_payment_method():
    response = api.get_payment_method(context['partner'], context['user'])

    response = api.get_payments(context['partner'], context['user'])
