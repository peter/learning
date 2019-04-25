import pytest
import test.config as config
from test.util import deep_get
import test.superscription.client_api as client_api
import test.superscription.api as api
import test.partner.api as partner_api
import test.user.api as user_api
from test.assert_helper import assert_equal

context = {}

STATUSES = {'NO_SUBSCRIPTION', 'EXPIRING_SUBSCRIPTION', 'ACTIVE_SUBSCRIPTION'}
PRODUCT_ID = '00001QTPAC'

def current_product_ids(history):
    addons = deep_get(history, 'current.addons')
    return addons and list(map(lambda a: deep_get(a, 'product.id'), addons))

def test_setup():
    email, password, user_id, partner_id = config.credentials()
    context['user_id'] = user_id
    context['partner'] = partner_api.get(partner_id).json()
    context['user_token'] = user_api.login(context['partner']['clientApiToken'], email, password).json()['token']

def test_client_api_get_subscription():
    data = client_api.get_subscription(context['user_id'], context['partner']['clientApiToken'], context['user_token']).json()
    assert_equal(data['status'] in STATUSES, True, 'user should have a subscription status')

def test_get_subscription():
    data = api.get_subscription(context['user_id'], context['partner']['id']).json()
    assert_equal(data['status'] in STATUSES, True, 'user should have a subscription status')

def test_get_history():
    data = api.get_history(context['user_id'], context['partner']['id']).json()
    print('user product IDS', current_product_ids(data))
    assert_equal(len(current_product_ids(data)) > 0, True, 'user should have current product IDs')

def test_add_and_cancel():
    cancel_data = {
        'productIds': [PRODUCT_ID],
        'hardCancel': True,
        'message': 'api-test (peter.marklund@my-app.com): test cancel',
        'source': 'internal',
        'billingPeriods': [],
        'sendEmail': False
    }
    api.cancel(context['user_id'], context['partner']['id'], cancel_data)

    data = api.get_history(context['user_id'], context['partner']['id']).json()
    product_ids = current_product_ids(data)
    print('user product IDS', current_product_ids(data))
    assert_equal(PRODUCT_ID in product_ids, False, 'user does not have product yet')

    add_data = {
        'productIds': (product_ids + [PRODUCT_ID]),
        'message': 'api-test (peter.marklund@my-app.com)',
        'source': 'internal',
        'sendEmail': False
    }
    api.add(context['user_id'], context['partner']['id'], add_data)

    data = api.get_history(context['user_id'], context['partner']['id']).json()
    print('user product IDS', current_product_ids(data))
    assert_equal(PRODUCT_ID in current_product_ids(data), True, 'user has product after add')

    cancel_data = {
        'productIds': [PRODUCT_ID],
        'hardCancel': True,
        'message': 'api-test (peter.marklund@my-app.com): test cancel',
        'source': 'internal',
        'billingPeriods': [],
        'sendEmail': False
    }
    api.cancel(context['user_id'], context['partner']['id'], cancel_data)

    data = api.get_history(context['user_id'], context['partner']['id']).json()
    print('user product IDS', current_product_ids(data))
    assert_equal(PRODUCT_ID in product_ids, False, 'user does not have product after cancel')
    assert_equal(current_product_ids(data), product_ids, 'user has same products after cancel as when we started')
