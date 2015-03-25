from checkio_referee import RefereeCodeGolf
from checkio_referee import covercodes

import settings
import settings_env
from tests import TESTS


class Referee(RefereeCodeGolf):
    TESTS = TESTS
    DEFAULT_MAX_CODE_LENGTH = 250
    BASE_POINTS = 25
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "golf"
    ENV_COVERCODE = {
        "python_2": covercodes.py_2_str,
        "python_3": None,
        "javascript": None
    }
