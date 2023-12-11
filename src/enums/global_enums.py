from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = 'Received status code is not to expected'
    VALUES_NOT_EQUAL = 'Number is not equal to expected'
    WRONG_ELEMENT_COUNT = 'Number of items is not equal to expected'