import logging
import os

import pytest

import dabah.service.utils.config as config

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


@pytest.fixture
def clean_env_str_var():
    os.environ.pop("TEST_GET_STR", None)
    yield
    os.environ.pop("TEST_GET_STR", None)


@pytest.mark.parametrize("env_value", ["True", "true", "truE", "YES", "yes", "y", "1"])
@pytest.mark.usefixtures("clean_env_bool_var")
def test_get_bool_true(env_value):
    os.environ["TEST_GET_BOOL"] = env_value
    cfg = config.EnvironmentConfig()

    assert cfg.getBool("TEST_GET_BOOL")


@pytest.mark.parametrize("env_value", ["FALSE", "false", "NO", "no", "n", "0"])
@pytest.mark.usefixtures("clean_env_bool_var")
def test_get_bool_false(env_value):
    os.environ["TEST_GET_BOOL"] = env_value
    cfg = config.EnvironmentConfig()

    assert not cfg.getBool("TEST_GET_BOOL")


@pytest.mark.usefixtures("clean_env_int_var")
def test_get_int():
    os.environ["TEST_GET_INT"] = "4000"

    cfg = config.EnvironmentConfig()
    assert cfg.getInt("TEST_GET_INT") == 4000


@pytest.mark.usefixtures("clean_env_str_var")
def test_get_str():
    os.environ["TEST_GET_STR"] = "mystring"

    cfg = config.EnvironmentConfig()
    assert cfg.getStr("TEST_GET_STR") == "mystring"


@pytest.mark.usefixtures("clean_env_bool_var")
def test_get_bool_not_present():
    cfg = config.EnvironmentConfig()
    assert cfg.getBool("TEST_GET_BOOL") is None


@pytest.mark.usefixtures("clean_env_int_var")
def test_get_int_not_present():
    cfg = config.EnvironmentConfig()
    assert cfg.getInt("TEST_GET_INT") is None


@pytest.mark.usefixtures("clean_env_str_var")
def test_get_str_not_present():
    cfg = config.EnvironmentConfig()
    assert cfg.getStr("TEST_GET_STR") is None


@pytest.mark.usefixtures("clean_env_int_var")
def test_get_int_bad_value_raises_exception():
    os.environ["TEST_GET_INT"] = "NOT INT"

    cfg = config.EnvironmentConfig()
    with pytest.raises(ValueError):
        cfg.getInt("TEST_GET_INT")


def test_environment_config_validate():
    with pytest.raises(NotImplementedError):
        config.EnvironmentConfig(validate=True)
