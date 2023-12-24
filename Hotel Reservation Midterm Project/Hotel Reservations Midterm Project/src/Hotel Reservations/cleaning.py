import pandas as pd
def cleaning_method(df):
    """
    cleaning methods 
    see single line comments
    """
    #Update columns to the right dtype (reservation_status_date to datetime and is_canceled to bool)
    df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])
    
    # Fill missing values with a default value (e.g., False) before converting to bool
    df['is_canceled'] = df['is_canceled'].astype('bool')

    #In a new column named 'arrival_date', connect the year, month and day of month to one neat datetime - you will need to convert the columns
    #to strings first
    df['arrival_date'] = df.apply(lambda row: pd.to_datetime(f"{row['arrival_date_year']}-{row['arrival_date_month']}-{row['arrival_date_day_of_month']}", errors='coerce'), axis=1)

    #In a new col named 'direct_booking' fill with 'yes' if agent and company are NaN values, else fill with no.
    df['direct_booking']= df.apply(lambda row: 'yes' if pd.isna(row['agent']) and pd.isna(row['company']) else 'no', axis=1)

    #check which columns have nans and drop if 70%
    thresh = 0.7 * len(df)
    df = df.dropna(thresh=thresh, axis=1)

    #Fill the rest of the nans as follows: if it’s a number col fill the missing fields with the mean. (round it) , if its a string col fill it with the value of the row before (or after)
    num_cols = df.select_dtypes(include=['number']).columns
    string_cols = df.select_dtypes(include=['object']).columns
    df_copy = df.copy()
    df_copy[num_cols] = df_copy[num_cols].fillna(df[num_cols].mean().round())
    df_copy[string_cols] = df_copy[string_cols].fillna(method='ffill')



