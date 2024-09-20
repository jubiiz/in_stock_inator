import time

from bs4 import BeautifulSoup
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait


def ftf_availability(driver: WebDriver, url: str) -> int:
    soup = get_soup_from_link(driver, url)
    return get_quantity_from_ftf_soup(soup)


def ftf_just_say_hi(driver: WebDriver, url: str) -> int:
    print(f"I JUST REALLY WANTED TO SAY HI FOR THIS URL: {url}")
    return 0


def get_soup_from_link(driver: WebDriver, url: str) -> BeautifulSoup:
    driver.get(url)
    WebDriverWait(driver, 10)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    return soup


def get_card_name_from_ftf_soup(soup: BeautifulSoup) -> str:
    return soup.find_all("h1", class_="productView-title")[0].contents[0]


def get_quantity_from_ftf_soup(soup: BeautifulSoup) -> int:
    result = soup.find_all("div", class_="form-field--stock")[0]
    result = result.find("span").contents[0]
    return int(result)
