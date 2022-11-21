from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import re

# Substitute your google form URL here
GOOGLE_FORM_URL = "https://forms.gle/cKe3iAAmoFwFGFz79"
# Substitute your chrome web driver path here
# https://chromedriver.chromium.org/downloads
CHROME_DRIVER_PATH = r"D:\Documents (D Drive)\Project Future\Dependent Software\chromedriver.exe"

HEADER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4"
                  "147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


class NoBrokerFinder:
    """
    Scrapes NoBroker.com for listing info and automatically submits a form via google forms to save data
    """
    def __init__(self):
        # Change the NoBroker url to use for other locations that NoBroker is available on.
        self.response = requests.get(
            "https://www.nobroker.in/property/rent/bangalore/Bengaluru?searchParam=W3sibGF0IjoxMi45Njk5MzM0NDAzNjgxLCJs"
            "b24iOjc3LjU5ODE3NzAzMjg1MjIsInNob3dNYXAiOmZhbHNlLCJwbGFjZUlkIjoiQ2hJSmJVNjB5WEFXcmpzUjRFOS1VZWpEM19nIiwicG"
            "xhY2VOYW1lIjoiQmFuZ2Fsb3JlIiwiY2l0eSI6ImJhbmdhbG9yZSJ9XQ==&gclid=Cj0KCQjwl_SHBhCQARIsAFIFRVVEwsslR_EEjDSB8"
            "4ycer54LDM3ow58JhBa6yM8E3JD6Ld_7dP39LwaAmKYEALw_wcB&lat_lng=12.9715987,77.59456269999998&ef_id=Cj0KCQjwl_S"
            "HBhCQARIsAFIFRVVEwsslR_EEjDSB84ycer54LDM3ow58JhBa6yM8E3JD6Ld_7dP39LwaAmKYEALw_wcB:G:s&AL!5425!3!4466293533"
            "52!b!!g!!2bhk%20on%20rent%20in%20bangalore!274612484!20580380084=&radius=1.0",
            headers=HEADER)
        # Initiates BeautifulSoup4 to scrape web data from NoBroker
        self.data = self.response.text
        self.soup = BeautifulSoup(self.data, "html.parser")

        self.listings = self.soup.select(".nb__GZOZV")
        self.listings_info = []
        self._get_listing_details()

    def _get_listing_details(self):
        """
        A clean and store listing data into a hash table
        """
        for listing in self.listings:
            url = "https://www.nobroker.in" + listing.select_one(".nb__31beh").get("href")
            address = listing.select_one(".nb__2EXTx").get_text()
            temp = re.split('(\d+)', self.listings[0].select_one(".nb__3vqcl").get_text())
            price = "₹" + temp[1] + temp[2] + temp[3]

            self.listings_info.append({
                "url": url,
                "address": address,
                "price": price,
            })

    def submit_data_to_form(self):
        """
        Submit the listing data via google form
        """
        # Access your chrome web driver
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

        for n in range(len(self.listings_info)):
            # Access your google form
            driver.get(GOOGLE_FORM_URL)

            time.sleep(2)
            # Change appropriate xpath from your form
            address = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link = driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

            address.send_keys(self.listings_info[n]["address"])
            price.send_keys(self.listings_info[n]["price"])
            link.send_keys(self.listings_info[n]["url"])
            submit_button.click()


noBroker_finder = NoBrokerFinder()
print(noBroker_finder.listings_info)
noBroker_finder.submit_data_to_form()
