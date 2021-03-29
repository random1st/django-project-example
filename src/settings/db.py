__all__ = (
    "DATABASES",
)

from settings.config import Config

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": Config.DB_NAME.value,
        "HOST": Config.DB_HOST.value,
        "PORT": Config.DB_PORT.value,
        "USER": Config.DB_USER.value,
        "PASSWORD": Config.DB_PASSWORD.value,
    }
}
