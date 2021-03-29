import logging

from settings.base import DEBUG

__all__ = (
    "LOGGING",
)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "fmt": u"[%(asctime)s] %(levelname)s at {%(filename)s:%(lineno)d} in %(name)s - %(message)s",
        },
    },
    "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "json"}, },
    "loggers": {
        "": {
            "level": logging.INFO if DEBUG else logging.WARNING,
            "handlers": ["console", ],
        },
        "django.request": {"level": logging.ERROR, "handlers": ["console", ], },
        # 'django.db.backends': {'level': 'DEBUG', 'handlers': ['console'], },
    },
}
