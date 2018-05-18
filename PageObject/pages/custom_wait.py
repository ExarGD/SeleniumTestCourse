from selenium.webdriver.support.expected_conditions import _find_element


class TextToChange(object):
    def __init__(self, locator, text):
        self.locator = locator
        self.text = text

    def __call__(self, driver):
        actual_text = _find_element(driver, self.locator).text
        return actual_text != self.text
