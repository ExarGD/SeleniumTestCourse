import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from time import sleep

href = "http://localhost/litecart/en/create_account"


class testCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.wd = webdriver.Chrome()

    def test_1(self):
        self.wd.get(href)
        try:
            WebDriverWait(self.wd, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "middle"))
            )
            print('Successfully opened main page!')
        except:
            print("Too long to wait!")
            self.wd.quit()

    def test_2(self):
        self.wd.find_element_by_css_selector("tr:nth-of-type(1) td:nth-of-type(1) [type]").send_keys('Tax ID')
        self.wd.find_element_by_css_selector('tr:nth-of-type(1) td:nth-of-type(2) [type]').send_keys('Company')
        self.wd.find_element_by_css_selector('tr:nth-of-type(2) td:nth-of-type(1) [type]').send_keys('First Name')
        self.wd.find_element_by_css_selector('tr:nth-of-type(2) td:nth-of-type(2) [type]').send_keys('Second Name')
        self.wd.find_element_by_css_selector('tr:nth-of-type(3) td:nth-of-type(1) [type]').send_keys('Address')
        self.wd.find_element_by_css_selector('tr:nth-of-type(4) td:nth-of-type(1) [type]').send_keys('50003')
        self.wd.find_element_by_css_selector('tr:nth-of-type(4) td:nth-of-type(2) [type]').send_keys('Toronto')
        selectCountry = Select(self.wd.find_element_by_css_selector('[name="country_code"]'))
        selectCountry.select_by_visible_text('United States')
        selectState = Select(self.wd.find_element_by_css_selector('select[name="zone_code"]'))
        selectState.select_by_visible_text('Iowa')
        self.wd.find_element_by_css_selector('[name="email"]').send_keys('email@email.com')
        self.wd.find_element_by_css_selector('[name="phone"]').send_keys('+19876543210')
        self.wd.find_element_by_css_selector('[name="password"]').send_keys('password')
        self.wd.find_element_by_css_selector('[name="confirmed_password"]').send_keys('password')
        self.wd.find_element_by_css_selector('[name="create_account"]').click()
        sleep(3)

    def test_3(self):
        self.wd.find_element_by_css_selector('#box-account [href="http\:\/\/localhost\/litecart\/en\/logout"]').click()
        self.wd.find_element_by_css_selector('[name="email"]').send_keys('email@email.com')
        self.wd.find_element_by_css_selector('[name="password"]').send_keys('password')
        self.wd.find_element_by_css_selector('[name="login"]').click()


    @classmethod
    def tearDownClass(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()