from enums import hotel, reservation_status, deposit_type, arrival_date_month
from entities import Guest
class Reservation:
    def __init__(self, data_row, hotel, reservation_status, deposit_type, arrival_date_month):
        """
        constructor for the Reservation class
        """
        self.data_row = data_row
        self.hotel=self.convert_enum(hotel, hotel)
        self.is_canceled=data_row["is_canceled"]
        self.lead_time=data_row["lead_time"]
        self.arrival_date_year=data_row["arrival_date_year"]
        self.arrival_date_month=self.convert_enum(arrival_date_month, arrival_date_month)
        self.arrival_date_week_number=data_row["arrival_date_week_number"]
        self.arrival_date_day_of_month=data_row["arrival_date_day_of_month"]
        self.stays_in_weekend_nights=data_row["stays_in_weekend_nights"]
        self.stays_in_week_nights=data_row["stays_in_week_nights"]
        self.meal=data_row["meal"]
        self.market_segment=data_row["market_segment"]
        self.distribution_channel=data_row["distribution_channel"]
        self.is_repeated_guest=data_row["is_repeated_guest"]
        self.previous_cancellations=data_row["previous_cancellations"]
        self.previous_bookings_not_canceled=data_row["previous_bookings_not_canceled"]
        self.reserved_room_type=data_row["reserved_room_type"]
        self.assigned_room_type=data_row["assigned_room_type"]
        self.booking_changes=data_row["booking_changes"]
        self.deposit_type=self.convert_enum(deposit_type, deposit_type)
        self.agent=data_row["agent"]
        self.company=data_row["company"]
        self.days_in_waiting_list=data_row["days_in_waiting_list"]
        self.customer_type=data_row["customer_type"]
        self.adr=data_row["adr"]
        self.required_car_parking_spaces=data_row["required_car_parking_spaces"]
        self.total_of_special_requests=data_row["total_of_special_requests"]
        self.reservation_status=self.convert_enum(reservation_status, reservation_status)
        self.reservation_status_date=data_row["reservation_status_date"]
        self.arrival_date=data_row["arrival_date"]
        self.direct_booking=data_row["direct_booking"]
        self.guest= Guest(data_row)

    def convert_enum(self, value, enum_class):
        return enum_class[value.upper()]

    def __str__(self):
        return f"Hotel type: {self.hotel}, Canceled: {self.is_canceled}, Lead Time: {self.lead_time}, Arrival Year: {self.arrival_date_year}, Arrival Month= {self.arrival_date_month}, \
        Arrival Week: {self.arrival_date_week_number}, Arrival day of Month: {self.arrival_date_day_of_month}, Number of Weekend Nights: {self.stays_in_weekend_nights}, Number of Week Nights: {self.stays_in_week_nights}, \
        Meal: {self.meal}, Market Segment: {self.market_segment}, Distribution Channel: {self.distribution_channel}, Repeated Guest: {self.is_repeated_guest}, \
        Previous Cancellations: {self.previous_cancellations}, Previous Bookings: {self.previous_bookings_not_canceled}, Reserved Room: {self.reserved_room_type}, \
        Assigned Room: {self.assigned_room_type}, Booking Changes: {self.booking_changes}, Deposit Type: {self.deposit_type}, Agent: {self.agent}, Company: {self.company}, \
        Number of day in the Waiting List: {self.days_in_waiting_list}, Customer Type: {self.customer_type}, Adr: {self.adr}, Required Car Parking: {self.required_car_parking_spaces}, \
        Special Requests: {self.total_of_special_requests}, Reservation Status: {self.reservation_status}, Reservation Status Date: {self.reservation_status_date}, \
        Direct Booking: {self.direct_booking}, Guest: {self.guest}" 

