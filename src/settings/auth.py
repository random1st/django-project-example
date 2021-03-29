__all__ = (
    "AUTH_USER_MODEL",
    "AUTHENTICATION_BACKENDS",
)

import logging


logger = logging.getLogger(__name__)
AUTH_USER_MODEL = "core.BaseUser"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
)

