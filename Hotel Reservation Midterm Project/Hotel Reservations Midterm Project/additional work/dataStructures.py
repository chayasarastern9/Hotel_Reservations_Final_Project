import random 
import pandas as pd
import numpy as np
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
import concurrent.futures

# path for csv 
file_path = 'Hotel Reservation Midterm Project\Hotel Reservations Midterm Project\src\Hotel Reservations\hotel_bookings.csv'
na_values = ['undefined',  'none']
# Read the CSV file into a DataFrame
df = pd.read_csv(file_path, na_values= na_values)

#create list of ten random numbers 
num_int_list=[1,2,3,4,5,6,7,8,9,10]

def lookup_function(list1, list2):
    """
    Count how many times a number from list1 exists in list2.

    Parameters:
    - list1: The list containing numbers to check.
    - list2: The list to check against.

    Returns:
    - A dictionary where keys are numbers from list1, and values are the counts of occurrences in list2.
    """
    counts_int_dict = {}
    for number in list1:
        counts_int_dict[number] = list2.count(number)
    return counts_int_dict

lead_time_list = df['lead_time'].tolist()
result_int_dict = lookup_function(num_int_list, lead_time_list)

# Display the result
print(result_int_dict)