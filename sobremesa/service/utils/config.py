import logging
import os

from dotenv import find_dotenv, load_dotenv

logger = logging.getLogger(__name__)


class ServiceConfigInterface:
    def __init__(self, validate=False):
        if validate:
            self.validate()

    def getStr(self, key: str):
        raise NotImplementedError

    def getBool(self, key: str):
        raise NotImplementedError

    def getInt(self, key: str):
        raise NotImplementedError

    def validate(self):
        raise NotImplementedError


class EnvironmentConfig(ServiceConfigInterface):
    def __init__(self, validate=False) -> None:
        super().__init__(validate)

        # Parse .env file, load all environment variables
        load_dotenv(find_dotenv(usecwd=True), verbose=True)

    def getStr(self, key: str) -> str | None:
        """Get string value. If key does not exist in environment, return None."""
        return os.environ.get(key)

    def getBool(self, key: str) -> bool | None:
        """Get boolean value. If key does not exist in environment, return None.

        Truthy values: [true, yes, y, 1]
        Falsy values: [false, no, n, 0]
        Values are case-insensitive.
        """
        value = os.environ.get(key)

        if isinstance(value, str):
            if value.lower() in ["true", "yes", "y", "1"]:
                return True
            elif value.lower() in ["false", "no", "n", "0"]:
                return False
        return None

    def getInt(self, key: str) -> int | None:
        """Get integer value. If value is not an integer or key does not exist in environment, return None"""
        value = os.environ.get(key)

        if isinstance(value, str):
            return int(value)
        return None

    def getEnv(self):
        """Return all environment variables."""
        return os.environ

    def dump(self):
        """Dump environment variables to a string."""
        return "\n".join(
            [f"{key}={value}" for key, value in sorted(os.environ.items())]
        )
