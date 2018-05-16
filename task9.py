import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from time import sleep

href = "http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1"


class testCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        dc = DesiredCapabilities.CHROME
        dc['loggingPrefs'] = {'browser': 'SEVERE'}
        self.wd = webdriver.Chrome(desired_capabilities=dc)

    def test_1(self):
        self.wd.get(href)
        self.wd.find_element_by_name("username").send_keys("admin")
        self.wd.find_element_by_name("password").send_keys("admin")
        self.wd.find_element_by_name("login").click()
        try:
            WebDriverWait(self.wd, 10).until(
                EC.presence_of_element_located((By.ID, "sidebar"))
            )
            print('Logged in!')
        except:
            print("Too long to wait!")

    def test_2(self):
        rows = self.wd.find_elements_by_css_selector('.dataTable td:nth-of-type(3) a')
        for k in range(3, rows.__len__()):
            rows = self.wd.find_elements_by_css_selector('.dataTable td:nth-of-type(3) a')
            rows[k].click()
            self.wd.get(href)
        for l in self.wd.get_log("browser"):
            print(l)
        self.assertTrue(len(self.wd.get_log("browser"))>0, "There are some SEVERE level errors!")


    @classmethod
    def tearDownClass(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()