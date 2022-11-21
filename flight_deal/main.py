from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint

# call the data manager class
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# call the flight search class
flight_search = FlightSearch()
# call the notification manager class
notification_manager = NotificationManager()

# put your origin city IATA here
ORIGIN_CITY_IATA = "MNL"

# cycle through the sheet data
for row in sheet_data:
    # checks if there's an empty cell in the sheet
    if row["iataCode"] == "":
        from flight_search import FlightSearch
        # call the flight search class
        flight_search = FlightSearch()
        for city in sheet_data:
            city["iataCode"] = flight_search.get_destination_code(city["city"])
        # update the self.destination_data dictionary with the latest data
        data_manager.destination_data = sheet_data
        data_manager.update_destination_code()

# date/time parameters for your flight search
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# check for available flight for your destination parameters
for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )