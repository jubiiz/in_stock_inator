from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://example.com")
driver.quit()