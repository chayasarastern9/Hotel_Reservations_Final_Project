from sqll import database_actions
from entities import Reservation, Guest
from sqlalchemy import create_engine, text
def get_top_agents_reservations_in_country(country):
    """
    This function gets the top ten reservations for the top agent for a specific country from a query

    parameters:
    country(str):the country that the user chose

    variables:
    sql_query_str(str): turns the sql query into a string literal 
    df_results(data frame): the query is turned into a dataframe 
    reservation_objects( reservation array): an array of reservation objrcys is created

    return:
    reservation_objects 
    """
    sql_query_str = """ WITH AgentBookings AS (
    SELECT TOP 1 agent, COUNT(R.ReservationId) AS total_bookings, G.country
    FROM dbo.Reservation R WITH(NOLOCK)
	JOIN dbo.Guest G WITH(NOLOCK) ON R.GuestId=G.GuestId
    WHERE G.country = """+'country'+"""
    GROUP BY R.agent, G.country
    ORDER BY total_bookings DESC
    )

    SELECT TOP 10 G.*
    FROM dbo.Reservation R WITH(NOLOCK)
    JOIN dbo.Guest G WITH(NOLOCK) ON R.GuestId = G.GuestId
    JOIN AgentBookings AB ON R.agent = AB.agent 
    AND G.country=AB.country
    ORDER BY R.ReservationId """
    df_results=database_actions.query(sql_query_str)
    def create_reservation_objects(df):
        """
        Parameter:
        df(data frame): the dataframe that was created by the query

        Return:
        reservation_objects: array of reservation objects
        """
        reservation_objects = []
        for index, row in df.iterrows():
            reservation = Reservation(row)
            reservation_objects.append(reservation)
        return reservation_objects
    reservation_objects = create_reservation_objects(df_results) 
    return reservation_objects
 

def get_reservation_year_adr(year, bottom, top):
    """
    this function gets a list of reservations from a certain year that have a adr within a certain range 
    parameters:
    year(int): year the user selected 
    bottom(int): bottom of the range the user selected 
    top(int): top of the range the user selected 

    variables:
    sql_query_str(str): turn the sql query into a string literal 
    df_results(data frame): the query is turned into a dataframe 
    reservation_objects( reservation array): an array of reservation objrcys is created

    return:
    reservation_objects 
    """
    sql_query_str="""SELECT R.*, G.*
    FROM dbo.Reservation R WITH(NOLOCK)
    JOIN dbo.Guest G WITH(NOLOCK) ON R.GuestId = G.GuestId
    WHERE R.arrival_date_year = """+year+""""
    AND R.adr BETWEEN """+bottom+""" AND"""+ top+"""
    AND R.is_canceled = 0"""
    df_results=database_actions.query(sql_query_str)
    def create_reservation_objects(df):
        """
        Parameter:
        df(data frame): the dataframe that was created by the query

        Return:
        reservation_objects: array of reservation objects
        """
        reservation_objects = []
        for index, row in df.iterrows():
            reservation = Reservation(row)
            reservation_objects.append(reservation)
        return reservation_objects
    reservation_objects = create_reservation_objects(df_results) 
    return reservation_objects
    

def get_connection_children_nights():
    """
    this function shows the connection between the number of children and the average nights, this informtion is from a query 

    Variales:
    sql_query(str): turn the sql query into a string literal
    df_results(data frame): the query is turned into a dataframe 
    reservation_objects( reservation array): an array of reservation objrcys is created

    return:
    reservation_objects 
    """
    sql_query_str="""SELECT G.children, AVG(R.stays_in_week_nights + R.stays_in_weekend_nights) AS AvgNights
    FROM dbo.Guest G WITH(NOLOCK) 
    JOIN dbo.Reservation R WITH(NOLOCK) ON G.GuestId=R.GuestId
    GROUP BY G.children, R.stays_in_week_nights, R.stays_in_weekend_nights;"""
    df_results=database_actions.query(sql_query_str)
    def create_reservation_objects(df):
        """
        Parameter:
        df(data frame): the dataframe that was created by the query

        Return:
        reservation_objects: array of reservation objects
        """
        reservation_objects = []
        for index, row in df.iterrows():
            reservation = Reservation(row)
            reservation_objects.append(reservation)
        return reservation_objects
    reservation_objects = create_reservation_objects(df_results) 
    return reservation_objects

def get_count_country(country):
    """
    This function uses a query to get the number of reservations from the country the user originates from 

    Parameters:
    country(str): the country the user chose 

    Variables:
    sql_query(str): turn the sql query into a string literal
    df_results(data frame): the query is turned into a dataframe 
    reservation_objects( reservation array): an array of reservation objrcys is created

    return:
    reservation_objects 
    """
    sql_query_str="""SELECT COUNT(G.Guestid), G.country
    FROM dbo.Guest G WITH(NOLOCK)
    WHERE G.country="""+'country'+"""
    GROUP BY G.country"""
    df_results=database_actions.query(sql_query_str)
    def create_reservation_objects(df):
        """
        Parameter:
        df(data frame): the dataframe that was created by the query

        Return:
        reservation_objects: array of reservation objects
        """
        reservation_objects = []
        for index, row in df.iterrows():
            reservation = Reservation(row)
            reservation_objects.append(reservation)
        return reservation_objects
    reservation_objects = create_reservation_objects(df_results) 
    return reservation_objects