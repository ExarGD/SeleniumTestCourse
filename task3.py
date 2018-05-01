import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

href = "http://localhost/litecart/admin/?app=countries&doc=countries"
links = []

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
        countries = self.wd.find_elements_by_css_selector('td:nth-of-type(5)')
        c_list = []
        for country in countries:
            c_list.append(country.get_attribute('innerText'))
        c_list_unsorted = c_list
        c_list.sort()
        self.assertEqual(c_list, c_list_unsorted, "Countries are unsorted")

    def test_3(self):
        countries = self.wd.find_elements_by_class_name('row')
        for country in countries:
            name = country.find_element_by_css_selector('td:nth-of-type(5) a')
            zone = country.find_element_by_css_selector('td:nth-of-type(6)')
            if zone.get_attribute('innerText') != '0':
                links.append(name.get_attribute('href'))
        s_list = []
        for link in links:
            self.wd.get(link)
            states = self.wd.find_elements_by_css_selector('.dataTable td:nth-of-type(3)')
            for state in states:
                s_list.append(state.get_attribute('innerText'))
            s_list_unsorted = s_list
            s_list.sort()
            self.assertEqual(s_list, s_list_unsorted, "States are unsorted")

    def test_5(self):
        href = "http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones"
        self.wd.get(href)
        links.clear()
        states = self.wd.find_elements_by_css_selector('.row td:nth-of-type(3) a')
        for state in states:
            links.append(state.get_attribute('href'))
        s_list = []
        for link in links:
            self.wd.get(link)
            states = self.wd.find_elements_by_css_selector('.dataTable td:nth-of-type(3) [selected]')
            for state in states:
                s_list.append(state.get_attribute('innerText'))
            s_list_unsorted = s_list
            s_list.sort()

            self.assertEqual(s_list, s_list_unsorted, "GeoZones are unsorted")

    @classmethod
    def tearDownClass(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
