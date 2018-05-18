from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from pages.custom_wait import TextToChange
from pages.item_list import ItemList


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.item_list = ItemList(self.driver)

    def quit(self):
        self.driver.quit()

    def add_items_to_cart(self):
        self.item_list.open()
        for i in range(0, 3):
            self.item_list.select_new_item.click()
            if len(self.item_list.select_dropdown) > 0:
                Select(self.driver.find_element_by_name("options[Size]")).select_by_visible_text("Small")
            self.item_list.add_to_cart.click()
            WebDriverWait(self.driver, 5).until(TextToChange((By.CSS_SELECTOR, "span.quantity"), str(i)))
            self.item_list.open()

    def remove_items_from_cart(self):
        self.item_list.open_cart.click()
        for i in range(0, 5):
            if len(self.item_list.remove_button) > 0:
                self.driver.find_element_by_css_selector('[name=remove_cart_item]').click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "em")))

    def get_quantity(self):
        self.item_list.open()
        return self.item_list.items_quantity
