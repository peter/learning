import pytest
from urllib.parse import urlparse, parse_qs
import test.config as config
import test.ads.api as api
import test.partner.api as partner_api
import test.user.api as user_api
from test.json import pretty_json
from test.util import deep_get, deep_set
from test.assert_helper import assert_equal

NON_EXISTANT_ID = 'this-id-doesnt-exist'
PARTNER_ID = 'example'
VOD_ID = 'api-test-playable-id'
VOD_SETTINGS = {
    'freeUsersOnly': False,
    'preroll': {'mobile': 'http://preroll.mobile?VPI=MP4&app[name]=REPLACE_ME', 'web': 'http://preroll.web?VPI=MP4&app[name]=REPLACE_ME'},
    'intervalroll': {'initial': 1, 'interval': 5, 'url': {'mobile': 'http://intervalroll.mobile'}}
}
CHANNEL_ID = '12474'
BROADCAST_ID = '9297573d-c983-4367-99c1-543d314f3949'
context = {}

def default_url(url):
    return deep_get(url, 'mobile')

def test_setup():
    email, password, _, _ = config.credentials()
    context['partner'] = partner_api.get(PARTNER_ID).json()
    context['clientApiToken'] = context['partner']['clientApiToken']
    api.internal_delete(PARTNER_ID, VOD_ID)
    assert_equal(api.internal_create(PARTNER_ID, VOD_ID, 'vod', 'api-test-viewable-id', VOD_SETTINGS).status_code, 200, 'create test VOD status')
    user = user_api.login(context['clientApiToken'], email, password).json()
    context['user_id'] = user['userId']
    context['user_token'] = user['token']
    print('user_id=%s, user_token=%s' % (context['user_id'], context['user_token']))
    context['user_info'] = {'gender': 'm', 'yearOfBirth': 1974}
    user_api.set_dynamic(context['user_id'],
                         context['clientApiToken'],
                         context['user_token'],
                         context['user_info'])

def test_override():
    data = api.public_get(VOD_ID, context['partner']).json()
    assert_equal(deep_get(data, 'preroll'), deep_get(VOD_SETTINGS, 'preroll.mobile'), 'preroll_url')

def test_defaults():
    partner_id = context['partner']['id']
    defaults = {'preroll': {'mobile': 'http://defaults.preroll.mobile'}}
    api.internal_defaults_delete(partner_id)
    api.internal_defaults_create(partner_id, defaults)

    data = api.public_get(NON_EXISTANT_ID, context['partner']).json()
    assert_equal(data, api.ad_settings_for_device(defaults), 'should be default ad settings with default device URLs')

    api.internal_defaults_delete(partner_id)

def test_device_type_mobile():
    data = api.public_get(VOD_ID, context['partner'], device_type='mobile').json()
    assert_equal(deep_get(data, 'preroll'), deep_get(VOD_SETTINGS, 'preroll.mobile'), 'preroll_url')
    assert_equal(deep_get(data, 'intervalroll.url'), deep_get(VOD_SETTINGS, 'intervalroll.url.mobile'), 'intervalroll_url')

def test_device_type_web():
    data = api.public_get(VOD_ID, context['partner'], device_type='web').json()
    assert_equal(deep_get(data, 'preroll'), deep_get(VOD_SETTINGS, 'preroll.web'), 'preroll_url')
    assert_equal(deep_get(data, 'intervalroll'), None, 'intervalroll_url')

def test_device_type_other():
    data = api.public_get(VOD_ID, context['partner'], device_type='foobar').json()
    assert_equal(deep_get(data, 'preroll'), deep_get(VOD_SETTINGS, 'preroll.mobile'), 'preroll_url')

def test_no_default_404():
    partner_id = context['partner']['id']
    api.internal_defaults_delete(partner_id)
    response = api.public_get(NON_EXISTANT_ID, context['partner'])
    assert_equal(response.status_code, 404, 'status_code')

def test_user_age_gender():
    data = api.public_get(VOD_ID, context['partner'], user_token=context['user_token']).json()
    # http://client-api.tvoli.com/api/ads/v1/vast-tracking/my-app/DQQ1O0YK89N9J99K302FRZUIGUSR/unknown?vastUrl=http%3A%2F%2Fpreroll.mobile%3Fuser%5Bgender%5D%3Dm%26user%5Byob%5D%3D1974', 'intervalroll': {'url': 'http://client-api.tvoli.com/api/ads/v1/vast-tracking/my-app/DQQ1O0YK89N9J99K302FRZUIGUSR/unknown?vastUrl=http%3A%2F%2Fintervalroll.mobile%3Fuser%5Bgender%5D%3Dm%26user%5Byob%5D%3D1974
    api_url = urlparse(deep_get(data, 'preroll'))
    assert_equal(api_url.hostname, urlparse(config.api_global_url()).hostname, 'api url hostname')
    assert_equal(api_url.path, f'/api/ads/v1/vast-wrapper/{context["partner"]["id"]}/{context["user_id"]}/unknown', 'api url path')
    url_string = parse_qs(api_url.query)['vastUrl'][0]
    url = urlparse(url_string)
    preroll_url = VOD_SETTINGS['preroll']['mobile']
    yob = str(context['user_info']['yearOfBirth'])
    gender = str(context['user_info']['gender'])
    url_string_expect = f'{preroll_url}&user[gender]={gender}&user[yob]={yob}'
    assert_equal(url_string, url_string_expect, 'vastUrl query param should be correct')
    query = parse_qs(url.query)
    expected_url = urlparse(deep_get(VOD_SETTINGS, 'preroll.mobile'))
    assert_equal(url.scheme, expected_url.scheme, 'url scheme')
    assert_equal(url.hostname, expected_url.hostname, 'url hostname')
    expected_query = {
        'user[yob]': yob,
        'user[gender]': gender
    }
    for param in expected_query:
        assert_equal(deep_get(query, [param, 0]), expected_query[param], 'expected param %s' % param)

def test_user_with_missing_age_gender():
    empty_user_info = {}
    user_api.set_dynamic(context['user_id'],
                         context['clientApiToken'],
                         context['user_token'],
                         empty_user_info)
    data = api.public_get(VOD_ID, context['partner'], user_token=context['user_token']).json()
    api_url = urlparse(deep_get(data, 'preroll'))
    url = urlparse(parse_qs(api_url.query)['vastUrl'][0])
    assert_equal(api_url.hostname, urlparse(config.api_global_url()).hostname, 'api url hostname')
    query = parse_qs(url.query)
    expected_url = urlparse(deep_get(VOD_SETTINGS, 'preroll.mobile'))
    assert_equal(url.scheme, expected_url.scheme, 'url scheme')
    assert_equal(url.hostname, expected_url.hostname, 'url hostname')
    expected_query = {
        'user[yob]': None,
        'user[gender]': None
    }
    for param in expected_query:
        assert_equal(deep_get(query, [param, 0]), expected_query[param], 'expected param %s' % param)

def test_free_users_only():
    response = api.public_get(VOD_ID, context['partner'], user_token=context['user_token'])
    assert_equal(response.status_code, 200, 'status_code before setting freeUsersOnly=true')

    updated_vod_settings = deep_set(VOD_SETTINGS, 'freeUsersOnly', True)
    api.internal_update(context['partner']['id'], VOD_ID, updated_vod_settings)

    assert_equal(deep_get(api.internal_get(context['partner']['id'], VOD_ID).json(), 'adSettings.freeUsersOnly'),
                 True,
                 'internal_get after update of freeUsersOnly')

    response = api.public_get(VOD_ID, context['partner'], user_token=context['user_token'])
    assert_equal(response.status_code, 404, 'status_code after setting freeUsersOnly=true')

def test_frequency_cap():
    frequencyCap = 3
    device = 'unknown'
    updated_vod_settings = deep_set(VOD_SETTINGS, 'frequencyCap', frequencyCap)
    api.internal_update(context['partner']['id'], VOD_ID, updated_vod_settings)
    assert_equal(deep_get(api.internal_get(context['partner']['id'], VOD_ID).json(), 'adSettings.frequencyCap'),
                 frequencyCap,
                 'internal_get after update of frequencyCap')

    response = api.public_get(VOD_ID, context['partner'], user_token=context['user_token'])
    assert_equal(response.status_code, 200, 'status_code API user first time')
    api.public_get_tracking(context['partner'], context['user_id'], device)
    response = api.public_get(VOD_ID, context['partner'], user_token=context['user_token'])
    assert_equal(response.status_code, 404, 'status_code API user second time')

def test_vast_wrapper():
    device = 'unknown'
    vast_url = 'https://search.spotxchange.com/vast/2.00/218908?VPI=MP4&app[name]=REPLACE_ME&app[bundle]=REPLACE_ME&app[storeurl]=REPLACE_ME&device[ifa]=REPLACE_ME&ip_addr=REPLACE_ME&cb=REPLACE_ME&player_width=REPLACE_ME&player_height=REPLACE_ME'
    response = api.public_get_vast_wrapper(context['partner'], context['user_id'], device, vast_url)
    assert_equal(response.status_code, 200, 'vast wrapper status_code')
    assert_equal(response.headers['content-type'], 'application/xml;charset=utf-8', 'vast wrapper content-type')
    assert_equal(vast_url in response.text, True, f'vast_url={vast_url} should be in response')
    trackingUrl = config.api_global_url() + f'/ads/v1/vast-tracking/{context["partner"]["id"]}/{context["user_id"]}/{device}'
    assert_equal(trackingUrl in response.text, True, f'trackingUrl={trackingUrl} should be in response', response.text)

# Example VAST XML:
# <?xml version="1.0" encoding="UTF-8"?>
# <VAST version="3.0">
#   <Ad id="wrapper1">
#     <Wrapper>
#       <AdSystem>MyApp Icarus</AdSystem>
#       <VASTAdTagURI>
#         <![CDATA[
#         http://this-is-the-vast-url.example
#         ]]>
#       </VASTAdTagURI>
#       <Impression>
#         <![CDATA[
#         http://client-api.tvoli.com/api/ads/v1/vast-tracking/my-app/DQQ1O0YK89N9J99K302FRZUIGUSR/unknown
#         ]]>
#       </Impression>
#     </Wrapper>
#   </Ad>
# </VAST>
