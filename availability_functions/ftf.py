from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time


def ftf_availability(driver: WebDriver, url: str) -> int:
    soup = get_soup_from_link(driver, url)
    return get_quantity_from_ftf_soup(soup)


def get_soup_from_link(driver: WebDriver, link: str) -> BeautifulSoup:
    driver.get(link)
    WebDriverWait(driver, 10)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    return soup


def get_card_name_from_ftf_soup(soup: BeautifulSoup) -> str:
    return soup.find_all("h1", class_="productView-title")[0].contents[0]


def get_quantity_from_ftf_soup(soup: BeautifulSoup) -> int:
    result = soup.find_all("div", class_="form-field--stock")[0]
    result = result.find("span").contents[0]
    return int(result)