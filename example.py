from scraper import Scraper
from htmlparser import Parser
from selenium.webdriver.common.by import By
import sys
#from config import chromedriver
from util import print_time, Elapsed


def test():
    if(len(sys.argv) < 3):
      raise Exception("Script must be called with two arguments, the path to chromedriver and the path to firebase config")

    chromedriver = sys.argv[1]

    elapsed = Elapsed()

    scraper = Scraper(chromedriver, headless=True)
    test_url = "https://96hpr.csb.app"

    try:
        scraper.open_page(test_url)
        html = scraper.get_outerhtml(
            By.XPATH, "/html/body/div/div/table/tbody")
        parsed = Parser(html, log_each_n=10)
        template = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
        parsed.extract_data_from_table(template, [0], True)
        print_time(f"Extracted data")
    finally:
        scraper.close()
        elapsed.end()


if __name__ == "__main__":
    test()
