import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

href = "http://localhost/litecart/en/"


class testCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.wd = webdriver.Safari()

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
        duck = self.wd.find_element_by_css_selector('#box-campaigns li.product')
        # ---Проверка цен---
        name = duck.find_element_by_css_selector('.name').get_attribute('innerText')
        regular_price = duck.find_element_by_css_selector('s.regular-price').get_attribute('innerText')
        discount_price = duck.find_element_by_css_selector('strong.campaign-price').get_attribute('innerText')
        # self.assertEqual(
        #     duck.find_element_by_css_selector('s.regular-price').value_of_css_property('text-decoration-line'),
        #     'line-through', "Regular price is not strikethrough")
        #---Safari---
        self.assertEqual(
            duck.find_element_by_css_selector('s.regular-price').value_of_css_property('text-decoration'),
            'line-through', "Regular price is not strikethrough")

        # ---Проверка цвета
        color_reg = duck.find_element_by_css_selector('s.regular-price').value_of_css_property('color')
        color_reg = color_reg.lstrip('rgba(')
        color_reg = color_reg.rstrip(', 1)')
        color_reg = color_reg.split(', ')
        self.assertTrue(color_reg[0] == color_reg[1] == color_reg[2], 'Color is not gray!')
        print(color_reg)

        color_disc = duck.find_element_by_css_selector('strong.campaign-price').value_of_css_property('color')
        color_disc = color_disc.lstrip('rgba(')
        color_disc = color_disc.rstrip(', 1)')
        color_disc = color_disc.split(', ')
        self.assertTrue(color_disc[1] == color_disc[2] == '0', 'Color is not red!')
        print(color_disc)

        # ---Проверка жирности---
        # self.assertEqual(
        #     duck.find_element_by_css_selector('strong.campaign-price').value_of_css_property('font-weight'),
        #     '700', "Discount price is not bold")

        # ---Firefox---
        # self.assertEqual(
        #     duck.find_element_by_css_selector('strong.campaign-price').value_of_css_property('font-weight'),
        #     '900', "Discount price is not bold")

        #---Safari---
        self.assertEqual(
            duck.find_element_by_css_selector('strong.campaign-price').value_of_css_property('font-weight'),
            'bold', "Discount price is not bold")

        # ---Проверка размера шрифта---
        self.assertTrue(
            float(duck.find_element_by_css_selector('s.regular-price').value_of_css_property('font-size').rstrip('px')) <
            float(duck.find_element_by_css_selector('strong.campaign-price').value_of_css_property('font-size').rstrip('px')),
            "Old price isn't smaller!")

        # ---Проверки на странице товара---
        self.wd.get('http://localhost/litecart/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1')
        inDuck = self.wd.find_element_by_css_selector('#box-product')
        inName = inDuck.find_element_by_css_selector('h1.title').get_attribute('innerText')
        self.assertEqual(name, inName, "Names are not equal!")

        inRegPrice = inDuck.find_element_by_css_selector('.regular-price').get_attribute('innerText')
        self.assertEqual(regular_price, inRegPrice, "Regular prices are not equal")

        inDiscPrice = inDuck.find_element_by_css_selector('.campaign-price').get_attribute('innerText')
        self.assertEqual(discount_price, inDiscPrice, "Discounted prices are not equal")

    @classmethod
    def tearDownClass(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()