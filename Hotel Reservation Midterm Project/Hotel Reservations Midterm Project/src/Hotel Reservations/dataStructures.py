import random 
import pandas as pd
import numpy as np
from collections import Counter
from concurrent.futures import ProcessPoolExecutor

# path for csv 
file_path = 'hotel_bookings.csv'
na_values = ['undefined',  'none']
# Read the CSV file into a DataFrame
df = pd.read_csv(file_path, na_values= na_values)

#create list of ten random numbers 
num_list=[random.randrange(1, 10) for_in range(10)]

def map_function(num):
    return num, 1

def reduce_function(results):
    return dict(Counter(dict(results)))

def lookup_function(new_data, column_data):
    with ProcessPoolExecutor() as executor:
        mapped_results = list(executor.map(map_function, new_data))
        grouped_data = {}
        for key, value in mapped_results:
            grouped_data.setdefault(key, []).append(value)
        reduced_result = list(executor.map(reduce_function, grouped_data.values()))
        result = reduce_function(reduced_result)
        return result

lead_time_array = np.array(df['lead_time'])
result = lookup_function(numbers, lead_time_array)

# Display the result
print(result)