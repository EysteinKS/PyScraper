from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import chromedriver
from util import print_time


class Scraper:
    def __init__(self, chromedriver, headless=False):
        chrome_options = Options()
        if(headless):
            chrome_options.add_argument("--headless")

        self.driver = Chrome(chromedriver, options=chrome_options)

    # Opens a new browser at the selected url
    def open_page(self, url, wait_time=0):
        print_time(f"Opening url {url}")
        self.driver.get(url)

        if(wait_time > 0):
            self.driver.implicitly_wait(wait_time)

        print_time("Page loaded")

    def click_by_xpath(self, xpath, wait_time=10):
        element = WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable((By.XPATH, xpath)))
        print_time(f"Clicking element by xpath {xpath}")
        element.click()

    def get_page_source(self):
        return self.driver.page_source()

    def wait_for_element(self, by, value):
        print_time(f"Waiting for {by} {value}")
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, value)))

    # Use selenium By.any to find element by value
    def get_innerhtml(self, by, value):
        print_time(f"Getting innerHTML from {by} {value}")
        element = self.wait_for_element(by, value)
        innerhtml = element.get_attribute("innerHTML")
        return innerhtml

    # Use selenium By.any to find element by value
    def get_outerhtml(self, by, value):
        print_time(f"Getting outerHTML from {by} {value}")
        element = self.wait_for_element(by, value)
        outerhtml = element.get_attribute("outerHTML")
        return outerhtml

    def close(self):
        print_time("Closing browser")
        self.driver.quit()
