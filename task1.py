import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

href = "http://localhost/litecart/admin/"


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
            WebDriverWait(self.wd, 60).until(
                EC.presence_of_element_located((By.ID, "sidebar"))
            )
            print('Logged in!')
        except:
            print("Too long to wait!")

    def test_2(self):
        sidebar = self.wd.find_elements_by_id('app-')
        print(sidebar.__len__())
        for i in range(0, sidebar.__len__()):
            sidebar = self.wd.find_elements_by_id('app-')
            try:
                WebDriverWait(self.wd, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "#app- a"))
                )
                sidebar[i].find_element_by_css_selector('#app- a').click()
                try:
                    sub = self.wd.find_elements_by_css_selector('.docs li')
                    for k in range(0, sub.__len__()):
                        sub = self.wd.find_elements_by_css_selector('.docs li')
                        sub[k].find_element_by_css_selector('.docs a').click()
                except:
                    print("Subelement wasn't found")
                print("Success!")
            except:
                print("Can't find such element")


    @classmethod
    def tearDownClass(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()