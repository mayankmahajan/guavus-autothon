from utils.parser import ObjectRepository
from selenium import webdriver

class LoginPage:
    def __init__(self):
        self.locator = ObjectRepository(file_path="/Users/praveen.garg1/Autothon/guavus-autothon/actions/parser_login.csv")

    def login(self,driver):
        email = self.locator.get_value("facebookemail")
        element = driver.find_element_by_id(email)
        element.send_keys("deepanshu")
        password = self.locator.get_value("facebookpass")
        element = driver.find_element_by_id(password)
        element.send_keys("ahuja")
        return True