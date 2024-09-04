import sys
import importlib

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.remote.webdriver import WebDriver


#https://www.facetofacegames.com/emrakul-the-world-anew-6-modern-horizons-3/
#https://www.facetofacegames.com/the-one-ring-451-borderless-bundle-the-lord-of-the-rings-tales-of-middle-earth/

URLS_TO_CHECK = [
    "https://www.facetofacegames.com/emrakul-the-world-anew-6-modern-horizons-3/",
    "https://www.facetofacegames.com/the-one-ring-451-borderless-bundle-the-lord-of-the-rings-tales-of-middle-earth/",
]


CHECKER_PATH = "/home/jubiiz/documents/code/in_stock_inator/availability_functions/ftf.py"


def main():
    spec = importlib.util.spec_from_file_location("ftf", CHECKER_PATH)
    module = importlib.util.module_from_spec(spec)
    sys.modules["ftf"] = module
    spec.loader.exec_module(module)

    checker = getattr(module, "ftf_availability")

    for url in URLS_TO_CHECK:
        driver = get_web_driver()
        result = checker(driver, url)
        res_as_int = int(result)
        print(res_as_int)





def get_web_driver() -> WebDriver:
    gecko_driver_path = '/usr/local/bin/geckodriver'  # Adjust if necessary
    service = Service(gecko_driver_path)
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    return webdriver.Firefox(service=service, options=options)



if __name__ == "__main__":
    main()

