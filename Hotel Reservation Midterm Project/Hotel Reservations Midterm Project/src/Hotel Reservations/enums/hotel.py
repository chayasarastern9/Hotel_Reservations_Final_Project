import pandas as pd
from enum import Enum, auto
class hotel(Enum):
    RESORT_HOTEL= auto()
    CITY_HOTEL=auto()

hotel_mapping={
    'Resort Hotel': hotel.RESORT_HOTEL,
    'City Hotel': hotel.CITY_HOTEL,
}