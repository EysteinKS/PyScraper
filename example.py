from scraper import Scraper
from selenium.webdriver.common.by import By
import sys

def test():
  if(len(sys.argv) < 3):
    raise Exception("Script must be called with two arguments, the path to chromedriver and the path to firebase config")

  chromedriver = sys.argv[1]
  scraper = Scraper(chromedriver)
  test_url = "https://blog.revathskumar.com/2011/10/python-list-all-packages-installed.html"

  try:
    scraper.open_page(test_url)
    scraper.click_by_xpath("/html/body/div/div/div[1]/div[1]/ul/li[1]/a[1]")
    html = scraper.get_outerhtml(By.CLASS_NAME, "posts")
    print(html)
  finally:
    scraper.close()

if __name__ == "__main__":
  test()