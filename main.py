import pandas as pd
import numpy as np
import cleaning
import database_actions

def main():
    # path for csv 
    file_path = 'hotel_bookings.csv'
    na_values = ['undefined',  'none']
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path, na_values= na_values)
    cleaning.cleaning_method(df)
    database_actions.create_tables_from_df(df)

if __name__ == "__main__":
    main()