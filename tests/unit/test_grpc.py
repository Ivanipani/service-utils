from dabah.service.utils.grpc import uuid_from_string


def test_uuid_from_string():
    assert uuid_from_string("123e4567-e89b-12d3-a456-426614174000")


def test_uuid_from_string_invalid():
    assert uuid_from_string(None) is None
    assert uuid_from_string(False) is None
    assert uuid_from_string("") is None
    assert uuid_from_string(bytes("abcdefg", "utf-8")) is None
