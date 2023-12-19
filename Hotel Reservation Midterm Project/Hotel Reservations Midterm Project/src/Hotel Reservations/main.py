import pandas as pd
import numpy as np
import cleaning
import database_actions

def main():
    print('aaaaa')
    setup()
#     #menu
#     def display_menu():
#         print("Please select from the menu below:")
#         print("1. View the best agent's top 10 reservations + guests in a specific country")
#         print("2. View reservations + guests that were not canceled that are within a specific price range (adr) for a specific year.")
#         print("3. ")

#     def option1():
#         country=input("Please enter a country: ")

#     def option2():
#         year=input("Please enter a year: ")
#         bottom= input("Please enter the bottom of your price range: ")
#         top= input("Please enter the top of your price range: ")

#     while True:
#         display_menu()
#         choice = input("Enter your choice (1-4): ")

#         if choice == '1':
#             option1()
#         elif choice == '2':
#             option2()
#         elif choice == '3':
#             option3()
#         else:
#             print("Invalid choice. Please enter a number between 1 and 4.")

def setup():
    # path for csv 
    print('bbbbbbbbbbbbbb')
    file_path = 'Hotel Reservation Midterm Project\Hotel Reservations Midterm Project\src\Hotel Reservations\hotel_bookings.csv'       
    # Read the CSV file into a DataFrame
    print('ddddddddddddddddddddddd')
    na_values=['undefined', 'none']
    df = pd.read_csv(file_path, na_values= na_values)
    cleaning.cleaning_method(df)
    database_actions.create_tables_from_df(df)

if __name__ == "__main__":
    main()