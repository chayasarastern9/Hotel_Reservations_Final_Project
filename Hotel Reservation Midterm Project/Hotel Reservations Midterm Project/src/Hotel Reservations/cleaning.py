import pandas as pd
def cleaning_method(df):
    #Update columns to the right dtype (reservation_status_date to datetime and is_canceled to bool)
    df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])
    #df['reservation_status_date'] = df['reservation_status_date'].astype('datetime')
    # Fill missing values with a default value (e.g., False) before converting to bool
    df['is_canceled'] = df['is_canceled'].astype('bool')


    #In a new column named 'arrival_date', connect the year, month and day of month to one neat datetime - you will need to convert the columns
    #to strings first
    df['arrival_date'] = df.apply(lambda row: pd.to_datetime(f"{row['arrival_date_year']}-{row['arrival_date_month']}-{row['arrival_date_day_of_month']}", errors='coerce'), axis=1)

    #In a new col named 'direct_booking' fill with 'yes' if agent and company are NaN values, else fill with no.
    df['direct_booking']= df.apply(lambda row: 'yes' if pd.isna(row['agent']) and pd.isna(row['company']) else 'no', axis=1)

    nan_cols = df.columns[df.isna().any()].tolist()
    thresh = 0.7 * len(df)
    df = df.dropna(thresh=thresh, axis=1)
    num_cols = df.select_dtypes(include=['number']).columns
    string_cols = df.select_dtypes(include=['object']).columns
    df_copy = df.copy()
    df_copy[num_cols] = df_copy[num_cols].fillna(df[num_cols].mean().round())
    df_copy[string_cols] = df_copy[string_cols].fillna(method='ffill')



