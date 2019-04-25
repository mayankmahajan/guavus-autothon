import copy
import locale
import os

from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.parser import ObjectRepository

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


class PeoplePage:
    def __init__(self, driver):
        self.locator = ObjectRepository(file_path=os.path.join(os.getcwd(), "actions", "people_handle.csv"))
        self.driver = driver

    def get_people_handle(self):
        inner_module = self.driver.find_element_by_xpath(self.locator.get_value('innerDiv'))
        return inner_module.find_elements_by_xpath(self.locator.get_value('personsClass'))

    def get_header(self):
        self.remove_login_window()
        user_module_handle = self.driver.find_element_by_xpath(self.locator.get_value('user_module'))
        return user_module_handle.find_element_by_xpath(self.locator.get_value('module_title')).text

    def remove_login_window(self):
        self.driver.find_element_by_xpath(self.locator.get_value('login_popup')).click()

    def get_people_info(self):
        biographies = []
        handles = self.get_people_handle()
        for i in range(0, 3):
            handle = handles[i]
            people = copy.deepcopy({})
            name = str(handle.text).split('\n')[0]
            handle_name = str(handle.text).split('\n')[1].lstrip('@')
            people["name"] = name
            people["handle_name"] = handle_name
            handletoHover = (handle.find_elements_by_xpath(self.locator.get_value('handletoHover')))[i]
            hover = ActionChains(self.driver).move_to_element(handletoHover)
            hover.perform()
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((By.ID, self.locator.get_value('hovercontainer'))))
            text_list = element.text.split('\n')
            people["follower_count"] = locale.atoi(str(text_list[text_list.index('Followers') + 1]))
            people["following_count"] = locale.atoi(str(text_list[text_list.index('Following') + 1]))
            biographies.append(people)
            self.remove_login_window()
        return biographies
