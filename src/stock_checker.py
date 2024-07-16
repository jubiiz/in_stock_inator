from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Path to the geckodriver binary
gecko_driver_path = '/usr/local/bin/geckodriver'  # Adjust if necessary

# Set up the FirefoxDriver
service = Service(gecko_driver_path)
options = webdriver.FirefoxOptions()
options.add_argument('--headless')

driver = webdriver.Firefox(service=service, options=options)

# Load the page
driver.get('https://www.facetofacegames.com/emrakul-the-world-anew-6-modern-horizons-3/')
#driver.get('https://www.facetofacegames.com/the-one-ring-451-borderless-bundle-the-lord-of-the-rings-tales-of-middle-earth/')

# Wait for the page to fully render (adjust timeout as needed)
WebDriverWait(driver, 10)

time.sleep(3)

# Get the page source after rendering
page_source = driver.page_source

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Close the WebDriver
driver.quit()

card_name = soup.find_all("h1", class_="productView-title")[0].contents[0]
# print(card_name)

result = soup.find_all("div", class_="form-field--stock")[0]
result = result.find("span").contents[0]
res_as_int = int(result)
print(res_as_int)