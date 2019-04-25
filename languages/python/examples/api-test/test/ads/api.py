import copy
import test.config as config
import test.http_client as http_client
from functools import reduce
from test.util import deep_get, deep_set

def internal_get_url(partner_id, playable_id):
    return '%s/ads/v1/overrides/%s/%s' % (config.url('ads-internal'), partner_id, playable_id)

def internal_list_url(partner_id):
    return '%s/ads/v1/overrides/%s' % (config.url('ads-internal'), partner_id)

def internal_defaults_get_url(partner_id):
    return '%s/ads/v1/defaults/%s' % (config.url('ads-internal'), partner_id)

def internal_defaults_list_url():
    return '%s/ads/v1/defaults' % (config.url('ads-internal'))

def ad_settings_for_device(ad_settings, device='mobile'):
    url_paths = [
        'preroll',
        'midroll.url',
        'intervalroll.url',
        'postroll'
    ]
    def build_result(result, path):
        device_path = path + '.' + device
        url = deep_get(result, path)
        device_url = deep_get(result, device_path)
        return deep_set(result, path, device_url) if url else result
    return reduce(build_result, url_paths, copy.deepcopy(ad_settings))

def public_get(playable_id, partner, device_type=None, user_token=None):
    url = '%s/ads/v1/%s' % (config.url('ads'), playable_id)
    # NOTE: api_global takes the MyApp-AccessToken (clientApiToken) header
    # and sets the MyApp-PartnerBackendSecret and MyApp-PartnerId headers
    headers = {
        'MyApp-PartnerId': partner['id'],
        'MyApp-PartnerBackendSecret': partner['backendSecret'],
        # 'MyApp-AccessToken': partner['clientApiToken'],
        'MyApp-Play-DeviceType': device_type
    }
    if user_token:
        headers['Authorization'] = 'Bearer %s' % (user_token)
    return http_client.get(url, headers=headers, valid_codes={200, 404, 400})

def public_get_vast_wrapper(partner, user_id, device_id, vast_url):
    url = '%s/ads/v1/vast-wrapper/%s/%s/%s' % (config.url('ads'), partner['id'], user_id, device_id)
    params = {'vastUrl': vast_url}
    headers = {'MyApp-PartnerId': partner['id']}
    return http_client.get(url, params=params, headers=headers, valid_codes={200})

def public_get_tracking(partner, user_id, device_id):
    url = '%s/ads/v1/vast-tracking/%s/%s/%s' % (config.url('ads'), partner['id'], user_id, device_id)
    headers = {'MyApp-PartnerId': partner['id']}
    return http_client.get(url, headers=headers, valid_codes={204})

def internal_get(partner_id, playable_id):
    return http_client.get(internal_get_url(partner_id, playable_id))

def internal_list(partner_id):
    return http_client.get(internal_list_url(partner_id))

def internal_create(partner_id, playable_id, playable_type, viewable_id, ad_settings):
    data = {
        'partnerId': partner_id,
        'playableId': playable_id,
        'viewableId': viewable_id,
        'playableType': playable_type
    }
    if (ad_settings):
        data['adSettings'] = ad_settings
    return http_client.post(internal_list_url(partner_id), data, valid_codes={200, 400})

def internal_update(partner_id, playable_id, ad_settings):
    return http_client.put(internal_get_url(partner_id, playable_id), ad_settings, valid_codes={200, 400})

def internal_delete(partner_id, playable_id):
    return http_client.delete(internal_get_url(partner_id, playable_id), valid_codes={200, 400})

def internal_defaults_get(partner_id):
    return http_client.get(internal_defaults_get_url(partner_id))

def internal_defaults_list():
    return http_client.get(internal_defaults_list_url())

def internal_defaults_create(partner_id, ad_settings):
    return http_client.post(internal_defaults_get_url(partner_id), ad_settings, valid_codes={200, 400})

def internal_defaults_update(partner_id, ad_settings):
    return http_client.put(internal_defaults_get_url(partner_id), ad_settings, valid_codes={200, 400})

def internal_defaults_delete(partner_id):
    return http_client.delete(internal_defaults_get_url(partner_id), valid_codes={200, 400})
