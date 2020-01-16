from scraper import Scraper
from parser import Parser
from selenium.webdriver.common.by import By
import sys
from config import chromedriver
from util import print_time, Elapsed


def test():
    """ if(len(sys.argv) < 3):
      raise Exception("Script must be called with two arguments, the path to chromedriver and the path to firebase config")

    chromedriver = sys.argv[1] """
    elapsed = Elapsed()

    scraper = Scraper(chromedriver, headless=True)
    test_url = "https://96hpr.csb.app"

    try:
        scraper.open_page(test_url)
        html = scraper.get_outerhtml(
            By.XPATH, "/html/body/div/div/table/tbody")
        parsed = Parser(html)
        template = {
            0: "A",
            1: "B",
            2: "C",
            3: "D",
            4: "E",
            5: "F",
            6: "G",
            7: "H",
            8: "I",
            9: "J",
            10: "K",
            11: "L",
            12: "M",
            13: "N",
            14: "O"
        }
        parsed.extract_data_from_table(template, pop=[0])
        print_time(f"Extracted data")
    finally:
        scraper.close()
        elapsed.end()


if __name__ == "__main__":
    test()
