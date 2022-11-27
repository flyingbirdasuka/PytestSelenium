from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from .Input import Input

class Slider:

    def __init__(self, driver, log):
        self.driver = driver
        self.log = log

    sliders = (By.TAG_NAME, "ion-range")
    icons = (By.TAG_NAME, "ion-icon")
    button = (By.CLASS_NAME, "allocate-button")
    total = (By.NAME, "ConstantSumSliders_total")
    next = (By.ID, "next_button")

    def slider_test(self):
        self.log.info('slider page')
        slider1 = self.driver.find_elements(*Slider.sliders)[0]
        move = ActionChains(self.driver)
        time.sleep(2)
        move.click_and_hold(slider1).move_by_offset(100, 0).release().perform()
        time.sleep(2)
        self.log.info('first slider point = ' +  slider1.get_attribute('value'))
        self.driver.find_elements(*Slider.icons)[0]
        self.driver.find_element(*Slider.button).click()
        total = self.driver.find_element(*Slider.total).get_attribute('value')
        self.log.info('totalSum = ' + total)
        self.driver.find_element(*Slider.next).click()

        inputPage = Input(self.driver, self.log)
        return inputPage