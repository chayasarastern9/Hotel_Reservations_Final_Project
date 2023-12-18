import pandas as pd
from enum import Enum, auto
class reservation_status(Enum):
    CHECK_OUT= auto()
    CANCLED= auto()
    NO_SHOW= auto()

reservation_status_mapping={
    'Check Out':reservation_status.CHECK_OUT,
    'Cancled': reservation_status.CANCLED,
    'No Show': reservation_status.NO_SHOW,
}