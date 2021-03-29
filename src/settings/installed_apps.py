from settings.base import DEBUG

__all__ = (
    "INSTALLED_APPS",
)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.contenttypes",
    "rest_framework",
    "health_check",
    "health_check.db",
    "django.contrib.postgres",
    "db.core",
    "db.animals",
    "db.auction",
]

if DEBUG:
    INSTALLED_APPS += ("drf_yasg",)
