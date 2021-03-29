# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
__all__ = (
    "SECURE_PROXY_SSL_HEADER",
    "BASE_DIR",
    "SECRET_KEY",
    "DEBUG",
    "ALLOWED_HOSTS",
    "ROOT_URLCONF",
    "WSGI_APPLICATION",
    "LANGUAGE_CODE",
    "TIME_ZONE",
    "USE_I18N",
    "USE_L10N",
    "USE_TZ",
    "STATIC_URL",
)
import os

from settings.config import Config

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = Config.SECRET_KEY.value

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = Config.DEBUG.value

ALLOWED_HOSTS = ["*"]

ROOT_URLCONF = "urls"

WSGI_APPLICATION = "wsgi.application"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = False

STATIC_URL = "/static/"
