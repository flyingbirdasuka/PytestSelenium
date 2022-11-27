from selenium.webdriver.common.by import By
import time
from .Count import Count

class Input:
    def __init__(self, driver, log):
        self.driver = driver
        self.log = log
    searchbar = (By.CLASS_NAME, "searchbar-input")
    dropdown = (By.CLASS_NAME, "clickable")
    next = (By.ID, "next_button")

    def input_test(self):
        self.log.info('input page')
        self.driver.find_element(*Input.searchbar).send_keys('ams')
        time.sleep(2)
        dropdown = self.driver.find_elements(*Input.dropdown)
        for city in dropdown:
            if city.text == 'Amsterdam':
                self.log.info('selected city = ' +  city.text)
                city.click()
                break
        self.driver.find_element(*Input.next).click()

        countPage = Count(self.driver, self.log)
        return countPage