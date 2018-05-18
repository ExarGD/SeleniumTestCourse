import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import _find_element
from selenium.webdriver.support.ui import Select
from time import sleep
import datetime

href = "http://localhost/litecart/en/"


class text_to_change(object):
    def __init__(self, locator, text):
        self.locator = locator
        self.text = text

    def __call__(self, driver):
        actual_text = _find_element(driver, self.locator).text
        return actual_text != self.text


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
        self.wd.get(href)
        for i in range(0, 3):
            self.wd.find_element_by_css_selector('#box-most-popular li:nth-of-type(1) .link').click()
            if len(self.wd.find_elements_by_css_selector('[name="options[Size]"]')) > 0:
                Select(self.wd.find_element_by_name("options[Size]")).select_by_visible_text("Small")
            old_qty = self.wd.find_element_by_css_selector('span.quantity').get_attribute('innerText')
            self.wd.find_element_by_css_selector('[name="add_cart_product"]').click()
            WebDriverWait(self.wd, 5).until(text_to_change((By.CSS_SELECTOR, "span.quantity"), str(i)))
            new_qty = self.wd.find_element_by_css_selector('span.quantity').get_attribute('innerText')
            self.assertNotEqual(old_qty, new_qty)
            self.wd.get(href)
            print(i)
        self.wd.find_element_by_id("cart").click()
        #WebDriverWait(self.wd, 5).until(EC.presence_of_element_located((By.NAME, "remove_cart_item")))
        for i in range(0, 3):
            if len(self.wd.find_elements_by_css_selector('[name=remove_cart_item]')) > 0:
                self.wd.find_element_by_css_selector('[name=remove_cart_item]').click()
        WebDriverWait(self.wd, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "em")))
        sleep(3)



    @classmethod
    def tearDownClass(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()