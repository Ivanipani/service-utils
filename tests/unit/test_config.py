import pytest
import os
import logging

import src.config as config

logger = logging.getLogger(__name__)


@pytest.fixture
def clean_env_bool_var():
    os.environ.pop("TEST_GET_BOOL", None)
    yield
    os.environ.pop("TEST_GET_BOOL", None)


@pytest.fixture
def clean_env_int_var():
    os.environ.pop("TEST_GET_INT", None)
    yield
    os.environ.pop("TEST_GET_INT", None)


@pytest.mark.parametrize("env_value", ["True", "true", "truE", "YES", "yes", "y"])
@pytest.mark.usefixtures("clean_env_bool_var")
def test_get_bool_true(env_value):
    os.environ["TEST_GET_BOOL"] = env_value
    cfg = config.EnvironmentConfig()

    assert cfg.getBool("TEST_GET_BOOL") == True


@pytest.mark.parametrize("env_value", ["FALSE", "false", "NO", "no", "n"])
@pytest.mark.usefixtures("clean_env_bool_var")
def test_get_bool_false(env_value):
    os.environ["TEST_GET_BOOL"] = env_value
    cfg = config.EnvironmentConfig()

    assert cfg.getBool("TEST_GET_BOOL") == False


@pytest.mark.usefixtures("clean_env_bool_var")
def test_get_bool_not_present():
    cfg = config.EnvironmentConfig()
    assert cfg.getBool("TEST_GET_BOOL") is None


@pytest.mark.usefixtures("clean_env_int_var")
def test_get_int():
    os.environ["TEST_GET_BOOL"] = "4000"

    cfg = config.EnvironmentConfig()
    assert cfg.getInt("TEST_GET_BOOL") == 4000


@pytest.mark.usefixtures("clean_env_int_var")
def test_get_int_bad_value_raises_exception():
    os.environ["TEST_GET_BOOL"] = "NOT INT"

    cfg = config.EnvironmentConfig()
    with pytest.raises(ValueError):
        cfg.getInt("TEST_GET_BOOL")


def test_environment_config_validate():
    os.environ["TEST_GET_BOOL"] = "NOT INT"

    with pytest.raises(NotImplementedError):
        cfg = config.EnvironmentConfig(validate=True)
