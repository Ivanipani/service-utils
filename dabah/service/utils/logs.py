import sys
import logging
import logging.config

from typing import Any


# USAGE
# import logging.config
# logging.config.dictConfig(get_standard_container_config())


def _get_standard_container_config(debug=False) -> dict[str, Any]:
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "%(asctime)s %(name)s:%(funcName)s:%(lineno)d %(levelname)s %(message)s",
                "style": "%",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "standard",
                "level": logging.DEBUG if debug else logging.INFO,
                "stream": sys.stdout,
            }
        },
        "loggers": {
            "": {"handlers": ["console"], "level": logging.DEBUG}
        },  # root logger
    }
    return config


def _set_dict_config(config) -> None:
    logging.config.dictConfig(config)


def set_standard_container_config(debug=False) -> None:
    _set_dict_config(_get_standard_container_config(debug))
