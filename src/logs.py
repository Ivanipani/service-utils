import sys
import logging
import logging.config

from typing import Any


# USAGE
# import logging.config
# logging.config.dictConfig(get_standard_container_config())


def get_standard_container_config(debug=False) -> dict[str, Any]:
    config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "{asctime} {name}:{funcName}:{lineno} {levelname} {message}",
                "style": "{",
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


def set_dict_config(config) -> None:
    logging.config.dictConfig(config)


def set_standard_container_config(debug=False) -> None:
    set_dict_config(get_standard_container_config(debug))
