import test.nibble.api as api
from test.assert_helper import assert_equal

partner_id = 'my-app'

def test_query():
    result = api.query(partner_id, 'kind:channel')
    assert_equal(result.status_code, 200)
    assert len(result.json()['items']) > 0
    assert result.json()['items'][0]['assetId']
    assert result.json()['items'][0]['title_en']
