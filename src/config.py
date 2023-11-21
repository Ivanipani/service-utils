#!/usr/bin/python
import os

from typing import Any


class ServiceConfigInterface:
    def __init__(self):
        self.validate()  # raise exception, cannot instantiate

    def get(self, key: str):
        raise NotImplementedError

    def validate(self):
        raise NotImplementedError


class EnvironmentConfigInterface(ServiceConfigInterface):
    def __init__(self) -> None:
        super().__init__()

    def get(key: str) -> str | None:
        return os.environ.get(key)
