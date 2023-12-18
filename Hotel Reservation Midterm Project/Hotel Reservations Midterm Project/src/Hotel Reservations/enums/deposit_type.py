import pandas as pd
from enum import Enum, auto
class deposit(Enum):
    DEPOSIT= auto()
    NO_DEPOSIT= auto()

deposit_mapping={
    'Deposit': deposit.DEPOSIT,
    'No Deposit': deposit.NO_DEPOSIT,
}
    