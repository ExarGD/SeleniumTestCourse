import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from time import sleep

href = "http://localhost/litecart/admin/?category_id=0&app=catalog&doc=edit_product"
uploadFile = "/batman-duck.jpg"

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
        self.wd.find_elements_by_css_selector('[name=status][value="1"]').click()
        self.wd.find_elements_by_css_selector('[name="name[en]"]').send_keys("Batman Duck")
        self.wd.find_element_by_css_selector('[name="code"]').send_keys("")



    @classmethod
    def tearDownClass(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()