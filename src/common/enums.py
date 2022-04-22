from enum import Enum


class StrEnum(str, Enum):
    pass


class EnvironmentSet(str, Enum):
    DEVELOPMENT = 'development'
    PRODUCTION = 'production'
    SANDBOX = 'sandbox'
    STAGING = 'staging'
