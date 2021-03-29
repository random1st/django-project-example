import os
from dataclasses import dataclass
from datetime import datetime
from typing import Callable


@dataclass
class Variable:
    name: str = None
    default: str = ""
    prevent_default: bool = False
    cast: Callable = str

    @property
    def value(self):
        v = os.getenv(self.name)
        if not v:
            if os.getenv("DEVELOP") or not self.prevent_default:
                v = self.default
            else:
                raise RuntimeError(f"Variable {self.name} is required")

        try:
            return self.cast(v) if v is not None else v
        except ValueError as e:
            raise RuntimeError(f"Variable {self.name} can not be converted to {self.cast} from value {v}") from e


class DefaultConfig:
    pass


#  APP_CONFIG #############################################################
class Config(DefaultConfig):
    ENV = Variable("ENV", "dev")

    # Debug
    DEBUG = Variable("DEBUG", "1", False, lambda v: bool(int(v)))

    # Security
    SUPERUSER_EMAIL = Variable("SUPERUSER_EMAIL", "admin@example.com", True)
    SUPERUSER_PASS = Variable("SUPERUSER_PASS", "admin", True)
    SECRET_KEY = Variable("SECRET_KEY", "%1dysxy4p35vg@i4lj9l$%tgzw=r1q^2t@g320@v#l1-)n%3+d", True)

    # Monitoring
    SENTRY_DSN = Variable("SENTRY_DSN", "", True)
    SENTRY_ENV = Variable("SENTRY_ENV", "", True)

    # DB and storages
    DB_NAME = Variable("DB_NAME", "db", True)
    DB_HOST = Variable("DB_HOST", "db", True)
    DB_PORT = Variable("DB_PORT", "5432", True, int)
    DB_USER = Variable("DB_USER", "user", True)
    DB_PASSWORD = Variable("DB_PASSWORD", "pass", True)

#################################################################################
