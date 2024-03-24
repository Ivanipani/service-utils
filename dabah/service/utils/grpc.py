import uuid
from typing import Union


class InvalidGrpcRequest(Exception):
    pass


def valid_uuid(data: str) -> Union[uuid.UUID, bool]:
    """Validate if a string or uuid.UUID is a valid UUID.

    Validity is checked by converting to string and back to uuid.UUID
    """
    try:
        return uuid.UUID(str(data))
    except ValueError:
        return False
