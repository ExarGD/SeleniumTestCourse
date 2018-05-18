from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class ItemList:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/en/")
        return self

    @property
    def select_new_item(self):
        return self.driver.find_element_by_css_selector('#box-most-popular li:nth-of-type(1) .link')

    @property
    def select_dropdown(self):
        return self.driver.find_elements_by_css_selector('[name="options[Size]"]')

    @property
    def items_quantity(self):
        return self.driver.find_element_by_css_selector('span.quantity').get_attribute('innerText')

    @property
    def add_to_cart(self):
        return self.driver.find_element_by_css_selector('[name="add_cart_product"]')

    @property
    def open_cart(self):
        return self.driver.find_element_by_id("cart")

    @property
    def remove_button(self):
        return self.driver.find_elements_by_css_selector('[name=remove_cart_item]')

    @property
    def phone_input(self):
        return self.driver.find_element_by_name("phone")

    @property
    def password_input(self):
        return self.driver.find_element_by_name("password")

    @property
    def confirmed_password_input(self):
        return self.driver.find_element_by_name("confirmed_password")

    @property
    def create_account_button(self):
        return self.driver.find_element_by_name("create_account")

    def select_country(self, country):
        self.driver.find_element_by_css_selector("[id ^= select2-country_code]").click()
        self.driver.find_element_by_css_selector(".select2-results__option[id $= %s]" % country).click()

    def select_zone(self, zone):
        self.wait.until(lambda d: d.find_element_by_css_selector("select[name=zone_code] option[value=%s]" % zone))
        Select(self.driver.find_element_by_css_selector("select[name=zone_code]")).select_by_value(zone)
