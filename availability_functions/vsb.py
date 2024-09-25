import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait


def vsb_course_availability(driver: WebDriver, item: dict) -> int:
    url = item["url"]
    semester = item["semester"]
    section = item["section"]

    driver.get(url)

    radio_buttons_divs = driver.find_elements(By.CLASS_NAME, "term_radio_item")
    for button_div in radio_buttons_divs:
        button_input = button_div.find_element(By.TAG_NAME, "input")
        if button_input.get_attribute("data-termlabel") == semester:
            button_input.click()
            break

    WebDriverWait(driver, 1)

    course_code_textfield = driver.find_element(By.ID, "code_number")
    course_code_textfield.send_keys("ECSE 326")
    course_code_send_button = driver.find_element(By.ID, "addCourseButton")
    course_code_send_button.click()

    time.sleep(1)

    course_table = driver.find_element(By.CLASS_NAME, "inner_legend_table")
    course_rows = course_table.find_elements(By.TAG_NAME, "tr")
    for row in course_rows:
        td = row.find_elements(By.TAG_NAME, "td")
        for cell in td:
            try:
                cell_text = cell.find_element(By.TAG_NAME, "strong").text
                if cell_text == section:
                    seats_span = cell.find_element(
                        By.XPATH, './/*[contains(@title, "seats")]'
                    )
                    seats_number_span = seats_span.find_element(By.TAG_NAME, "span")
                    seats_number = seats_number_span.text
                    break
            except NoSuchElementException:
                continue

    time.sleep(1)
    driver.quit()
    return seats_number
