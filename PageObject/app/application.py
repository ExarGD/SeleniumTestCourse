from selenium import webdriver
from pages.admin_page_logon import AdminPageLogOn
from pages.customers_page import CustomersPage
from pages.registration_page import RegistrationPage


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.registration_page = RegistrationPage(self.driver)
        self.admin_panel_login_page = AdminPageLogOn(self.driver)
        self.customer_list_page = CustomersPage(self.driver)

    def quit(self):
        self.driver.quit()

    def register_new_customer(self, customer):
        self.registration_page.open()
        self.registration_page.firstname_input.send_keys(customer.firstname)
        self.registration_page.lastname_input.send_keys(customer.lastname)
        self.registration_page.address1_input.send_keys(customer.address)
        self.registration_page.postcode_input.send_keys(customer.postcode)
        self.registration_page.city_input.send_keys(customer.city)
        self.registration_page.select_country(customer.country)
        self.registration_page.select_zone(customer.zone)
        self.registration_page.email_input.send_keys(customer.email)
        self.registration_page.phone_input.send_keys(customer.phone)
        self.registration_page.password_input.send_keys(customer.password)
        self.registration_page.confirmed_password_input.send_keys(customer.password)
        self.registration_page.create_account_button.click()

    def get_customer_ids(self):
        if self.admin_panel_login_page.open().check_right_page():
            self.admin_panel_login_page.enter_username("admin").enter_password("admin").submit_login()
        return self.customer_list_page.open().get_customer_ids()
