import test.offer.api as api
from test.assert_helper import assert_equal
from test.util import digest, parse_datetime, now

partner_id = 'example'

def test_crud():
    viewable_ids = list(api.search(partner_id).json())
    assert len(viewable_ids) > 1

    pack = {'name': 'API Test Pack' + digest(), 'viewables': [viewable_ids[0]]}
    result = api.create_pack(partner_id, pack)
    assert_equal(result.status_code, 201)
    pack_id = result.json()['id']
    assert pack_id
    created_at = parse_datetime(result.json()['createdAt'])
    assert created_at <= now()

    result = api.get_pack(partner_id, pack_id)
    assert_equal(result.status_code, 200)
    assert_equal(result.json()['id'], pack_id)
    assert_equal(result.json()['name'], pack['name'])
    assert_equal(result.json()['viewables'], pack['viewables'])

    result = api.list_packs(partner_id)
    assert_equal(result.status_code, 200)
    pack_ids = set([p['id'] for p in result.json()])
    assert pack_id in pack_ids

    update = {'action': 'add', 'viewables': [viewable_ids[1]]}
    result = api.update_pack(partner_id, pack_id, update)
    assert_equal(result.status_code, 200)

    update = {'action': 'remove', 'viewables': [viewable_ids[0]]}
    result = api.update_pack(partner_id, pack_id, update)
    assert_equal(result.status_code, 200)

    pack['viewables'] = [viewable_ids[1]]
    result = api.get_pack(partner_id, pack_id)
    assert_equal(result.status_code, 200)
    assert_equal(result.json()['id'], pack_id)
    assert_equal(result.json()['name'], pack['name'])
    assert_equal(result.json()['viewables'], pack['viewables'])

    timing = {
        'purchaseAvailableSince': '2012-12-20T00:00:00.00Z',
        'purchaseAvailableUntil': '2012-12-24T00:00:00.00Z'
    }
    pricing = {
        'upfrontPriceCents': 4900,
        'currency': 'SEK'
    }
    offer = {
        'packId': pack_id,
        'type': 'est',
        'timing': timing,
        'pricing': pricing,
        'regions': ['SE']
    }
    result = api.create_offer(partner_id, offer)
    assert_equal(result.status_code, 201)
    print('create offer', result.json())
    offer['offerId'] = result.json()['offerId']

    result = api.get_offer(partner_id, offer['offerId'])
    assert_equal(result.status_code, 200)
    assert_equal(result.json()['offerId'], offer['offerId'])
    assert_equal(result.json()['type'], offer['type'])
    assert_equal(result.json()['disabled'], False)

    result = api.list_offers(partner_id, pack_id)
    offer_ids = set([o['offerId'] for o in result.json()])
    assert offer['offerId'] in offer_ids

    result = api.update_offer(partner_id, offer['offerId'], {'disabled': True})
    assert_equal(result.status_code, 200)

    result = api.get_offer(partner_id, offer['offerId'])
    assert_equal(result.json()['disabled'], True)

    # NOTE: apparently it is not possible to re-enable a disabled offer.
    # result = api.update_offer(partner_id, offer['offerId'], {'disabled': False})
    # assert_equal(result.status_code, 200)

    # result = api.get_offer(partner_id, offer['offerId'])
    # assert_equal(result.json()['disabled'], False)
