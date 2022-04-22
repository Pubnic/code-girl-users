import os
import traceback
# import sentry_sdk
from common.enums import EnvironmentSet


def capture_exception(ex: Exception):
    if os.environ.get('ENVIRONMENT') != EnvironmentSet.DEVELOPMENT:
        # sentry_sdk.capture_exception(ex)
        traceback.print_exc()
    else:
        raise ex
