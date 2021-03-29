import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.redis import RedisIntegration

__all__ = (
    "SENTRY_DSN",
    "SENTRY_ENV",
)

from settings.config import Config

SENTRY_DSN = Config.SENTRY_DSN.value
SENTRY_ENV = Config.SENTRY_ENV.value

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        environment=SENTRY_ENV,
        integrations=[DjangoIntegration(), RedisIntegration(), ],
    )
