import os

from utils.parser import ObjectRepository


class LoginPage:
    def __init__(self):
        self.locator = ObjectRepository(file_path=os.path.join(os.getcwd(), "actions", "parser_login.csv"))

    def login(self, driver):
        email = self.locator.get_value("facebookemail")
        element = driver.find_element_by_id(email)
        element.send_keys("deepanshu")
        password = self.locator.get_value("facebookpass")
        element = driver.find_element_by_id(password)
        element.send_keys("ahuja")
        return True
