import os

from dotenv import load_dotenv

# Parse .env file, load all environment variables
load_dotenv()


class ServiceConfigInterface:
    def __init__(self):
        self.validate()  # raises exception, cannot instantiate

    def getStr(self, key: str):
        raise NotImplementedError

    def getBool(self, key: str):
        raise NotImplementedError

    def getInt(self, key: str):
        raise NotImplementedError

    def validate(self):
        raise NotImplementedError


class EnvironmentConfig(ServiceConfigInterface):
    def __init__(self) -> None:
        super().__init__()

    def getStr(self, key: str) -> str | None:
        return os.environ.get(key)

    def getBool(self, key: str) -> bool | None:
        value = os.environ.get(key)

        if isinstance(value, str):
            if value.lower() in ["true", "yes", "y"]:
                return True
            elif value.lower() in ["false", "no", "n"]:
                return False
        return None

    def getInt(self, key: str) -> int | None:
        value = os.environ.get(key)

        if isinstance(value, str):
            return int(value)
        return None

    def validate(self):
        pass
