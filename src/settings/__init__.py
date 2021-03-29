import os

import yaml

from settings.application import * # NOQA
from settings.base import * # NOQA
from settings.db import DATABASES # NOQA
from settings.installed_apps import INSTALLED_APPS  # NOQA
from settings.logging import * # NOQA
from settings.middleware import MIDDLEWARE # NOQA
from settings.rest_framework import REST_FRAMEWORK # NOQA
from settings.sentry import * # NOQA
from settings.templates import *  # NOQA
from settings.auth import * # NOQA
from settings.swagger import * # NOQA


try:
    data = yaml.safe_load(open("/version.yml"))

    APP_VERSION = data["APP_VERSION"]
except (OSError, ValueError):
    APP_VERSION = "unknown"
