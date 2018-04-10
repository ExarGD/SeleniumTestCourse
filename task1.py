import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

href = "http://127.0.0.1:8080/litecart/admin/"

class testCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.wd = webdriver.Chrome()


    def test_1(self):
        self.wd.get(href)
        self.wd.find_element_by_name("username").send_keys("admin")
        self.wd.find_element_by_name("password").send_keys("admin")
        #self.wd.find_element_by_name("remember_me").click()
        self.wd.find_element_by_name("login").click()
        try:
            WebDriverWait(self.wd, 30).until(EC.presence_of_element_located((By.CLASS, "header")))
        finally:
            self.wd.quit()


    def tearDownClass(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()