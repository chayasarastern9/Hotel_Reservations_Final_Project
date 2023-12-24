import pandas as pd
from enum import Enum, auto

#create an enum for the month 
class month(Enum):
    JAN=auto()
    FEB=auto()
    MARCH=auto()
    APRIL=auto()
    MAY=auto()
    JUNE=auto()
    JULY=auto()
    AUG=auto()
    SEP=auto()
    OCT=auto()
    NOV=auto()
    DEC=auto()

month_mapping={
    'January':month.JAN,
    'February':month.FEB,
    'March':month.MARCH,
    'April':month.APRIL,
    'May':month.MAY,
    'June':month.JUNE,
    'July':month.JULY,
    'August':month.AUG,
    'September':month.SEP,
    'October':month.OCT,
    'November':month.NOV,
    'December':month.DEC,
}