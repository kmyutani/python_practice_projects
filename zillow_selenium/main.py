from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

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


class ZillowFinder:
    """
    Scrapes Zillow.com for listing info and automatically submits a form via google forms to save data
    """
    def __init__(self):
        # Change the zillow url to use for other locations that zillow is available on.
        self.response = requests.get(
            "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Silicon%20"
            "Valley%20Blvd%20San%20Jose%2C%20CA%2095138%22%2C%22mapBounds%22%3A%7B%22west%22%3A-121.9426744505619%2C%"
            "22east%22%3A-121.80774860827674%2C%22south%22%3A37.2977989572856%2C%22north%22%3A37.377805520136754%7D%2"
            "C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%"
            "7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3"
            "A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%"
            "7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%2"
            "2value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%2"
            "2isListVisible%22%3Atrue%2C%22mapZoom%22%3A13%2C%22customRegionId%22%3A%22adde460fdbX1-CR1mttqyur8w41q_y"
            "apho%22%7D",
            headers=HEADER)
        # Initiates BeautifulSoup4 to scrape web data from zillow
        self.data = self.response.text
        self.soup = BeautifulSoup(self.data, "html.parser")

        self.listings = self.soup.select(".list-card-info")
        self.listings_info = []
        self._get_listing_details()

    def _get_listing_details(self):
        """
        A clean and store listing data into a hash table
        """
        for listing in self.listings:
            url = listing.select_one(".list-card-link").get("href")
            address = listing.select_one(".list-card-addr").get_text()
            price = listing.select_one(".list-card-price").get_text()

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


zillow_finder = ZillowFinder()
print(zillow_finder.listings_info)
zillow_finder.submit_data_to_form()
