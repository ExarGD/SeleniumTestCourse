import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import os
from time import sleep

href = "http://localhost/litecart/admin/?category_id=1&app=catalog&doc=edit_product"
uploadFile = os.path.abspath("batman-duck.jpg")

class testCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.wd = webdriver.Chrome()

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
        self.wd.get(href)
        self.wd.find_element_by_css_selector('[name=status][value="1"]').click()
        self.wd.find_element_by_css_selector('[name="name[en]"]').send_keys("Batman Duck")
        self.wd.find_element_by_css_selector('[name="code"]').send_keys("rd006")
        self.wd.find_element_by_css_selector('[type="checkbox"][value="2"]').click()
        Select(self.wd.find_element_by_css_selector('[name="default_category_id"]')).\
            select_by_visible_text('Subcategory')
        self.wd.find_element_by_css_selector('[name="product_groups[]"][value="1-3"]').click()
        self.wd.find_element_by_css_selector('[name=quantity]').send_keys('20')
        self.wd.find_element_by_css_selector('[type=file]').send_keys(uploadFile)
        self.wd.find_element_by_css_selector('[name=date_valid_from]').send_keys('15042018')
        self.wd.find_element_by_css_selector('[name=date_valid_to]').send_keys('20042018')

    def test_3(self):
        # self.wd.find_element_by_css_selector('[href="\#tab-information"]').click()
        self.wd.find_element_by_link_text("Information").click()
        WebDriverWait(self.wd, 3).until(
            EC.presence_of_element_located((By.NAME, "manufacturer_id"))
        )
        Select(self.wd.find_element_by_css_selector('[name=manufacturer_id]')).\
            select_by_visible_text('ACME Corp.')
        self.wd.find_element_by_css_selector('[name=keywords]').send_keys("batman, duck")
        self.wd.find_element_by_css_selector('[name="short_description[en]"]').send_keys("Batman Rubber Duck")
        self.wd.find_element_by_css_selector('.trumbowyg-editor').send_keys('Description')
        self.wd.find_element_by_css_selector('[name="head_title[en]"]').send_keys("Batman Duck")
        self.wd.find_element_by_css_selector('[name="meta_description[en]"]').send_keys('Meta Description')

    def test_4(self):
        # self.wd.find_element_by_css_selector('[href="\#tab-prices"]').click()
        self.wd.find_element_by_link_text("Prices").click()
        WebDriverWait(self.wd, 3).until(
            EC.presence_of_element_located((By.NAME, "purchase_price"))
        )
        self.wd.find_element_by_css_selector('[name="purchase_price"]').send_keys('25')
        Select(self.wd.find_element_by_css_selector('[name="purchase_price_currency_code"]')).\
            select_by_visible_text('US Dollars')
        self.wd.find_element_by_css_selector('[name="prices[USD]"]').send_keys('25')
        self.wd.find_element_by_css_selector('[name="prices[EUR]"]').send_keys('23')
        self.wd.find_element_by_css_selector('[name="gross_prices[USD]"]').send_keys('25')
        self.wd.find_element_by_css_selector('[name="gross_prices[EUR]"]').send_keys('23')
        self.wd.find_element_by_css_selector('[name="save"]').click()

    @classmethod
    def tearDownClass(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()