import database_actions
def get_top_agents_reservations_in_country(country):
    sql_query = """WITH AgentBookings AS (
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
    ORDER BY R.ReservationId"""
    database_actions.query(sql_query)

def get_reservation_year_adr(year, bottom, top):
    """SELECT R.*, G.*
    FROM dbo.Reservation R WITH(NOLOCK)
    JOIN dbo.Guest G WITH(NOLOCK) ON R.GuestId = G.GuestId
    WHERE R.arrival_date_year = """+year+""""
    AND R.adr BETWEEN """+bottom+""" AND"""+ top+"""
    AND R.is_canceled = 0"""

def get_connection_children_nights():
    """SELECT G.children, AVG(R.stays_in_week_nights + R.stays_in_weekend_nights) AS AvgNights
    FROM dbo.Guest G WITH(NOLOCK) 
    JOIN dbo.Reservation R WITH(NOLOCK) ON G.GuestId=R.GuestId
    GROUP BY G.children, R.stays_in_week_nights, R.stays_in_weekend_nights;"""

def get_count_country(country):
    """SELECT COUNT(G.Guestid), G.country
    FROM dbo.Guest G WITH(NOLOCK)
    WHERE G.country="""+'country'+"""
    GROUP BY G.country"""