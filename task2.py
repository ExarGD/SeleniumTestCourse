import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

href = "http://localhost/litecart/en/"


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
        blocks = self.wd.find_elements_by_class_name('box')
        for block in blocks:
            ducks = block.find_elements_by_class_name('product')
            for duck in ducks:
                    if duck.find_element_by_class_name('sticker'):
                        print('Found one!')
                    else:
                        print('Oops!')

    @classmethod
    def tearDownClass(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
