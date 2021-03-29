from settings.config import Config

__all__ = (
    "SUPERUSER_EMAIL",
    "SUPERUSER_PASS",
    "ENV",
)

SUPERUSER_EMAIL = Config.SUPERUSER_EMAIL.value
SUPERUSER_PASS = Config.SUPERUSER_PASS.value

ENV = Config.ENV.value
