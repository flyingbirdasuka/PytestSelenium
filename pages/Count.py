from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

class Count:
    def __init__(self, driver, log):
        self.driver = driver
        self.log = log

    options = (By.CLASS_NAME, "clickable")

    def count_test(self):
        self.log.info('count page')
        selectOptions = self.driver.find_elements(*Count.options)
        for i in range(6):
            if i != 5:
                selectOptions[i].click()
            if i == 5:
                className = selectOptions[i].find_element(By.CLASS_NAME, 'graphical_select').get_attribute("class")
                self.log.info('className of this 6th checkbox' + className)
                self.log.info(className.__contains__('checkbox'))
                try:
                    selectOptions[i].click()
                except WebDriverException:
                    self.log.info("Element is not clickable")

        self.driver.get_screenshot_as_file('screen.png')  # make a screenshot
        self.log.info('finished :)')