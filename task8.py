import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from time import sleep

href = "http://localhost/litecart/admin/?app=countries&doc=countries"

class getFirstOpenedWindow(object):
    def __init__(self, oldWindows):
        self.oldWindows = oldWindows

    def __call__(self, driver):
        currentWindows = driver.window_handles
        newWindows = list(set(currentWindows) - set(self.oldWindows))
        return newWindows[0] if len(newWindows) > 0 else None

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
        self.wd.find_element_by_css_selector(".button").click()
        WebDriverWait(self.wd, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1 .icon-wrapper")))
        main_window = self.wd.current_window_handle
        extLinks = self.wd.find_elements_by_css_selector(".fa-external-link")
        for link in extLinks:
            old_windows = self.wd.window_handles
            link.click()
            try:
                new_window = WebDriverWait(self.wd, 5).until(getFirstOpenedWindow(old_windows))
                self.wd.switch_to.window(new_window)
                self.wd.close()
                self.wd.switch_to.window(main_window)
            except:
                print("There is no other windows")


    @classmethod
    def tearDownClass(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()