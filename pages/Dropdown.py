from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .Slider import Slider

class Dropdown:
    def __init__(self, driver, log):
        self.driver = driver
        self.log = log
    con1 = (By.ID, "ConDropdown1")
    con2 = (By.ID, "ConDropdown2")
    con3 = (By.ID, "ConDropdown3")
    next = (By.ID, "next_button")

    def dropdown_test(self):
        self.log.info('dropdown page')
        assert self.driver.find_element(*Dropdown.con2).is_enabled() == False
        assert self.driver.find_element(*Dropdown.con3).is_enabled() == False
        self.driver.find_element(*Dropdown.con1).click()
        dropdown1 = Select(self.driver.find_element(*Dropdown.con1))
        dropdown1.select_by_visible_text('Jakarta')

        self.driver.find_element(*Dropdown.con2).click()
        dropdown2 = Select(self.driver.find_element(*Dropdown.con2))

        assert len(dropdown2.options) == 21  # check the length of the dropdown list
        dropdown2.select_by_visible_text('Jakarta Pusat')

        self.driver.find_element(*Dropdown.con3).click()
        dropdown3 = Select(self.driver.find_element(*Dropdown.con3))
        dropdown3.select_by_visible_text('Green Garden')
        self.driver.find_element(*Dropdown.next).click()  # go to the next question page

        sliderPage = Slider(self.driver, self.log)
        return sliderPage