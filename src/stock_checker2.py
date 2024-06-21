from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Set up Chrome WebDriver
chrome_options = ChromeOptions()
chrome_options.add_argument('--headless')  # Run Chrome in headless mode, no GUI needed
chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
service = ChromeService(executable_path='/path/to/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

# Load the page
driver.get('https://example.com')

# Wait for the page to fully render (adjust timeout as needed)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'selector-for-your-element')))

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