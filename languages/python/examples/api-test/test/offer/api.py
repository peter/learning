import test.http_client as http_client
import test.config as config
from test.type_spec import typeSpec, type_check, Enum
from requests.models import Response

def Pack(v):
    return type_check(v, {'name': str, 'viewables': [str]})

def PackUpdate(v):
    return type_check(v, {'action': Enum('add', 'remove'), 'viewables': [str]})

def Offer(v):
    return type_check(v, {
        'packId': str,
        'type': Enum('est', 'rental'),
        'timing': {'purchaseAvailableSince': '2012-12-20T00:00:00.00Z', 'purchaseAvailableUntil': '2012-12-24T00:00:00.00Z'},
        'pricing': {'upfrontPriceCents': 4900, 'currency': 'SEK'},
        'regions': [str]})

def OfferUpdate(v):
    return type_check(v, {'disabled': bool})

@typeSpec(str, dict)
def headers(partner_id):
    authorization = 'Bearer internal:{}'.format(config.backend_secret())
    return {'MyApp-PartnerId': partner_id, 'Authorization': authorization}

@typeSpec(str, Response)
def search(partner_id):
    url = '%s/offer/v1/search' % (config.url('offer'))
    return http_client.get(url, headers=headers(partner_id))

@typeSpec(str, Pack, Response)
def create_pack(partner_id, pack):
    url = '%s/offer/v1/packs' % (config.url('offer'))
    return http_client.post(url, pack, headers=headers(partner_id))

@typeSpec(str, str, Response)
def get_pack(partner_id, pack_id):
    url = '%s/offer/v1/packs/%s' % (config.url('offer'), pack_id)
    return http_client.get(url, headers=headers(partner_id))

@typeSpec(str, Response)
def list_packs(partner_id):
    url = '%s/offer/v1/packs' % (config.url('offer'))
    return http_client.get(url, headers=headers(partner_id))

@typeSpec(str, str, PackUpdate, Response)
def update_pack(partner_id, pack_id, update):
    url = '%s/offer/v1/packs/%s' % (config.url('offer'), pack_id)
    return http_client.patch(url, update, headers=headers(partner_id))

@typeSpec(str, Offer, Response)
def create_offer(partner_id, offer):
    url = '%s/offer/v1/offers' % (config.url('offer'))
    return http_client.post(url, offer, headers=headers(partner_id))

@typeSpec(str, str, Response)
def get_offer(partner_id, offer_id):
    url = '%s/offer/v1/offers/%s' % (config.url('offer'), offer_id)
    return http_client.get(url, headers=headers(partner_id))

@typeSpec(str, str, Response)
def list_offers(partner_id, pack_id):
    url = '%s/offer/v1/offers' % (config.url('offer'))
    params = {'packId': pack_id}
    return http_client.get(url, params=params, headers=headers(partner_id))

@typeSpec(str, str, OfferUpdate, Response)
def update_offer(partner_id, offer_id, update):
    url = '%s/offer/v1/offers/%s' % (config.url('offer'), offer_id)
    return http_client.patch(url, update, headers=headers(partner_id))
