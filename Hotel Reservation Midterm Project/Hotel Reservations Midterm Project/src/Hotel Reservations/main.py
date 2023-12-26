import pandas as pd
import numpy as np
from data_analysis import cleaning
from sqll import database_actions, queries
import logging



logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')




def main():
    """
    calls the setup function which creates the dataframe, cleans the data, and then puts the data into a sql database 
    calls the display_menu function 
    calls the option functions
    """
    setup()
    #menu
    def display_menu():
        """
        displays the menu
        """
        print("Please select from the menu below:")
        print("1. View the best agent's top 10 reservations + guests in a specific country")
        print("2. View reservations + guests that were not canceled that are within a specific price range (adr) for a specific year.")
        print("3. View whether the number of children impacts the number of nights.")
        print("4. View how many people from the same country as you made reservations.")

    def option1():
        """
        when the user chooses option 1 this function is called 
        it asks the user to enter a country and asigns the input to a variale and then calls another function to create the output
        variables:
        country_str(str): the country inputted by the user 
        response(str): the query string that will be outputted
        """
        country_str=input("Please enter a country: ")
        response_str=queries.get_top_agents_reservations_in_country(country_str)
        print(response_str)
        

    def option2():
        """
        when the user chooses option two this function is called
        asks the user to enter a year, a bottom and top number for a range, and aigns the input to variables and then calls another function to create the output 
        variables:
        year_int(int): year inputted
        bottom_int(int): bottom of range inputted 
        top_int(int): top of range inputted
        """
        year_int=input("Please enter a year: ")
        bottom_int= input("Please enter the bottom of your price range: ")
        top_int= input("Please enter the top of your price range: ")
        queries.get_reservation_year_adr(year_int, bottom_int, top_int)

    def option3():
        """
        when the user chooses option 3 this function is called
        prints a query showing if the numper of children impacts the number of nights
        """
        print("Now we will see if the number of children impacts the number of nights:")
        queries.get_connection_children_nights()
    
    def option4():
        """
        when the user chooses option 4 this function is called
        This function asks the user to enter the countryy he is from and then it asigns the input to a variable and then calls another function to create the output
        variable:
        country_str(str): country that the user inputs
        """
        country_str=input("Please enter the country you come from: ")
        queries.get_count_country(country_str)

    while True:
        display_menu()
        """
        displays the menu to the user and allows the user to pick a choice and then calls the function connected to that choice
        variable:
        choice_int(int): choice inputted by user
        """
        choice_int = input("Enter your choice (1-4): ")

        if choice_int == '1':
            option1()
        elif choice_int == '2':
            option2()
        elif choice_int == '3':
            option3()
        elif choice_int== '4':
            option4()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def setup():
    """
    this function is called at the beginning of main and it reads the csv file into a dataframe, it also calls the cleaning functions and transforms the dataframe into database tables
    varriable:
    file_path(str): file pathfor the csv file
    na_values(str array): array of words that should be defined as nan
    df(dataframe): the dataframe that is created
    """
   
    # path for csv 
    file_path = 'Hotel Reservation Midterm Project\Hotel Reservations Midterm Project\src\Hotel Reservations\hotel_bookings.csv'       
    # Read the CSV file into a DataFrame
    na_values=['undefined', 'none']
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.warning('The data frame is being created')
    df = pd.read_csv(file_path, na_values= na_values)
    logging.warning('The data frame is being cleaned')
    cleaning.cleaning_method(df)
    logging.warning('The tables are being created')
    database_actions.create_tables_from_df(df)

if __name__ == "__main__":
    main()