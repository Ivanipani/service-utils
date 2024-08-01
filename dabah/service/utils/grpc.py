import uuid


class InvalidGrpcRequest(Exception):
    pass


def uuid_from_string(data: str):
    """Create uuid.UUID object from string. If invalid, return None."""
    try:
        if not isinstance(data, str):
            return None
        return uuid.UUID(data)
    except ValueError:
        return None
