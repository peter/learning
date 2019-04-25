import pytest
import test.ads.api as api
from test.assert_helper import assert_equal

partner_id = 'api-test'
playable_id = 'api-test-playable-id'
playable_type = 'vod'
viewable_id = 'api-test-viewable-id'
ad_settings = {
    'preroll': {
        'mobile': 'http://preroll.mobile'
    }
}
ad_settings_invalid_url = {
    'preroll': {
        'mobile': 'preroll.mobile'
    }
}
updated_ad_settings = {
    'freeUsersOnly': True,
    'preroll': {
        'mobile': 'http://preroll.mobile.changed'
    }
}
ad_settings_full = {
    'freeUsersOnly': True,
    'frequencyCap': 3600,
    'preroll': {
        'mobile': 'http://preroll.mobile',
        'web': 'http://preroll.web'
    },
    'midroll': {
        'url': {
            'mobile': 'http://midroll.mobile',
            'web': 'http://midroll.web'
        },
        'offsets': [0, 10, 20, 30]
    },
    'intervalroll': {
        'url': {
            'mobile': 'http://intervalroll.mobile',
            'web': 'http://intervalroll.web'
        },
        'initial': 0,
        'interval': 10
    },
    'postroll': {
        'mobile': 'http://postroll.mobile',
        'web': 'http://postroll.web'
    }
}

def test_crud_overrides():
    api.internal_delete(partner_id, playable_id)
    api.internal_create(partner_id, playable_id, playable_type, viewable_id, ad_settings)

    overrides = api.internal_list(partner_id).json()
    override_ids = map(lambda o: o['playableId'], overrides)
    assert_equal(playable_id in override_ids, True, 'playable_id_in_list')

    override = api.internal_get(partner_id, playable_id).json()
    assert_equal(override['playableId'], playable_id, 'playable_id_in_get')
    assert_equal(override['partnerId'], partner_id)
    assert_equal(override['playableType'], playable_type)
    assert_equal(override['viewableId'], viewable_id)
    assert_equal(override['adSettings'], ad_settings)

    api.internal_update(partner_id, playable_id, updated_ad_settings)

    override = api.internal_get(partner_id, playable_id).json()
    assert_equal(override['adSettings'], updated_ad_settings)

    api.internal_delete(partner_id, playable_id)

    response = api.internal_get(partner_id, playable_id)
    assert_equal(response.status_code, 404, 'get should be 404 after delete')

def test_crud_defaults():
    api.internal_defaults_delete(partner_id)
    api.internal_defaults_create(partner_id, ad_settings)

    defaults = api.internal_defaults_list().json()
    partner_ids = map(lambda o: o['partnerId'], defaults)
    assert_equal(partner_id in partner_ids, True, 'partner_id_in_list')

    defaults = api.internal_defaults_get(partner_id).json()
    assert_equal(defaults['partnerId'], partner_id)
    assert_equal(defaults['adSettings'], ad_settings)

    api.internal_defaults_update(partner_id, updated_ad_settings)

    defaults = api.internal_defaults_get(partner_id).json()
    assert_equal(defaults['adSettings'], updated_ad_settings)

    api.internal_defaults_delete(partner_id)

    response = api.internal_defaults_get(partner_id)
    assert_equal(response.status_code, 404, 'get should be 404 after delete')

def test_create_defaults_invalid_url():
    api.internal_defaults_delete(partner_id)
    assert_equal(api.internal_defaults_create(partner_id, ad_settings_invalid_url).status_code, 400, 'invalid url create defaults')

def test_create_full():
    api.internal_delete(partner_id, playable_id)
    response = api.internal_create(partner_id, playable_id, playable_type, viewable_id, ad_settings_full)
    assert_equal(response.status_code, 200, "create full status")

    override = api.internal_get(partner_id, playable_id).json()
    assert_equal(override['playableId'], playable_id, 'playable_id_in_get')
    assert_equal(override['partnerId'], partner_id)
    assert_equal(override['playableType'], playable_type)
    assert_equal(override['viewableId'], viewable_id)
    assert_equal(override['adSettings'], ad_settings_full)

def test_create_empty_allowed():
    api.internal_delete(partner_id, playable_id)
    assert_equal(api.internal_create(partner_id, playable_id, playable_type, viewable_id, None).status_code, 200, 'create empty status code')

def test_create_double():
    api.internal_delete(partner_id, playable_id)

    api.internal_create(partner_id, playable_id, playable_type, viewable_id, ad_settings)
    response = api.internal_create(partner_id, playable_id, playable_type, viewable_id, {})
    assert_equal(response.status_code, 400, 'status on double create')

    override = api.internal_get(partner_id, playable_id).json()
    assert_equal(override['playableId'], playable_id, 'playable_id_in_get')
    assert_equal(override['partnerId'], partner_id)
    assert_equal(override['playableType'], playable_type)
    assert_equal(override['viewableId'], viewable_id)
    assert_equal(override['adSettings'], ad_settings)

    api.internal_delete(partner_id, playable_id)

def test_create_invalid_json():
    api.internal_delete(partner_id, playable_id)
    response = api.internal_create(partner_id, playable_id, playable_type, viewable_id, "{this-is-not-valid-json")
    assert_equal(response.status_code, 400, 'status for invalid json')

def test_create_invalid_schema():
    api.internal_delete(partner_id, playable_id)
    response = api.internal_create(partner_id, playable_id, playable_type, viewable_id, '{"foo": "this-is-not-a-valid-schema"}')
    assert_equal(response.status_code, 400, 'status for invalid schema')

def test_create_invalid_playable_id():
    api.internal_delete(partner_id, playable_id)
    response = api.internal_create(partner_id, None, playable_type, viewable_id, ad_settings)
    assert_equal(response.status_code, 400, 'status for invalid playable ID')

def test_create_invalid_playable_type():
    api.internal_delete(partner_id, playable_id)
    response = api.internal_create(partner_id, playable_id, 'foobar', viewable_id, ad_settings)
    assert_equal(response.status_code, 400, 'status for invalid playable type')

def test_update_invalid_schema():
    api.internal_delete(partner_id, playable_id).status_code
    assert_equal(api.internal_create(partner_id, playable_id, playable_type, viewable_id, ad_settings).status_code, 200)
    assert_equal(api.internal_update(partner_id, playable_id, '{"foo": "this-is-not-a-valid-schema"}').status_code, 400, 'status for invalid schema')



# TODO: create validation
# validatePresent(['partnerId', 'playableId', 'viewableId', 'playableType']),
# validatePlayableType,
# validateAdSettings,
# validateAdSettingsSchema(schema)

# TODO: update validation
# validatePresent(['partnerId', 'playableId']),
# validateAdSettings,
# validateAdSettingsSchema(schema)
