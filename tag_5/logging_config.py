import logging.config

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "%(levelname)s - %(message)s"},
        "detailed": {"format": "%(asctime)s | %(name)s | %(levelname)s | %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": "DEBUG",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "game.log",
            "formatter": "detailed",
            "level": "INFO",
            "encoding": "utf-8",
        },
    },
    "loggers": {
        "hero": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
        "inventory": {
            "handlers": ["console", "file"],
            "level": "WARNING",
            "propagate": False,
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}


def setup_logging() -> None:
    """Initialisiert die Logging-Konfiguration."""
    logging.config.dictConfig(LOGGING_CONFIG)
