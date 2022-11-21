import requests

TOKEN = "YOUR SHEETY API TOKEN HERE"
ENDPOINT_SHEETY = "YOUR SHEETY API ENDPOINT HERE"
# Token Authentication
HEADER = {
    "Authorization": TOKEN
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """
        Access the data from the sheety API
        """
        response = requests.get(ENDPOINT_SHEETY)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_code(self):
        """
        Update the data from the sheety API
        """
        # loop through the row in the data
        for row in self.destination_data:
            # creates the parameter needed for the sheety API
            # get the current value from the self.destination_data
            # and adds it to the new data to be updated in the sheety API
            new_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }
            response = requests.put(
                url=f"{ENDPOINT_SHEETY}/{row['id']}",
                json=new_data,
            )
            response.raise_for_status()
