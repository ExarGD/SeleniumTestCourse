import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

href = "https://www.google.com"

class testCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.wd = webdriver.Chrome()


    def test_1(self):
        self.wd.get(href)
        self.wd.find_element_by_name("q").send_keys("Selenium was here")
        self.wd.find_element_by_name("btnI").click()
        try:
            WebDriverWait(self.wd, 10).until(EC.title_is("Selenium was here - Google Search"))
        except:
            print("Title mismatch")
            self.wd.quit()

    def tearDownClass(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()