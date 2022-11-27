from baseclass.BaseClass import BaseClass
from pages.Dropdown import Dropdown

class Test_Selenium(BaseClass):
    def test_1(self):
        log = self.getLogger()
        dropdownPage= Dropdown(self.driver, log)
        sliderPage = dropdownPage.dropdown_test()
        inputPage = sliderPage.slider_test()
        countPage = inputPage.input_test()
        countTest = countPage.count_test()








