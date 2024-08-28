from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

#https://www.facetofacegames.com/emrakul-the-world-anew-6-modern-horizons-3/
#https://www.facetofacegames.com/the-one-ring-451-borderless-bundle-the-lord-of-the-rings-tales-of-middle-earth/

LINKS_TO_CHECK = [
    "https://www.facetofacegames.com/emrakul-the-world-anew-6-modern-horizons-3/",
    "https://www.facetofacegames.com/the-one-ring-451-borderless-bundle-the-lord-of-the-rings-tales-of-middle-earth/",
]


def main():
    print("main")
    driver = get_web_driver()
    print("soup")
    soup = get_soup_from_link(driver, "https://www.facetofacegames.com/emrakul-the-world-anew-6-modern-horizons-3/")
    print("qtt")
    result = get_quantity_from_ftf_soup(soup)
    res_as_int = int(result)
    print(res_as_int)


def get_web_driver() -> WebDriver:
    gecko_driver_path = '/usr/local/bin/geckodriver'  # Adjust if necessary
    service = Service(gecko_driver_path)
    print("options")
    options = webdriver.FirefoxOptions()
    print("firefox")
    options.set_preference('profile', '/home/jubiiz/documents/code/in_stock_inator/firefox_setup/profile')  # Replace with the actual path
    #options.add_argument('--headless')
    return webdriver.Firefox(service=service, options=options)


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

if __name__ == "__main__":
    main()

