import farmOS

from .test_credentials import valid_credentials

def test_invalid_login():
    farm = farmOS.farmOS('test.farmos.net', 'username', 'password')
    success = farm.authenticate()

    assert success is False

def test_valid_login():
    farm = farmOS.farmOS(**valid_credentials)
    success = farm.authenticate()

    assert success is True

def test_valid_record_request():
    """ Verifies that get_records pulls logs from the server """
    farm = farmOS.farmOS(**valid_credentials)
    farm.authenticate()
    logs = farm.get_records('log')

    assert len(logs) > 0
