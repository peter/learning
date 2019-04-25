import pytest
import test.partner.api as api
from test.assert_helper import assert_equal

def test_get():
    partner_id = 'my-app'
    partner = api.get(partner_id).json()
    assert_equal(partner['id'], partner_id, 'partner_id')

def test_404():
    partner_id = 'this-partner-does-not-exist-surely'
    response = api.get(partner_id)
    assert_equal(response.status_code, 404, ('get should be 404 for non-existant partner ID %s' % partner_id))
