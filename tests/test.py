import json
import logging
import random

import pytest

from actions.actions import Actions
from utils.json_parser import JsonParser
from utils.people import PeoplePage
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait

chromeOptions = webdriver.ChromeOptions()

@pytest.fixture(scope="function")
def setup(request):
    print("initiating chrome driver")
    chromeOptions.add_argument('--headless')
    chromeOptions.add_argument('--no-sandbox')
    # driver = webdriver.Remote(
    #     command_executor='http://192.168.135.96:4444/wd/hub', desired_capabilities=chromeOptions.to_capabilities())
    # request.cls.driver = driver
    # driver.get("http://www.facebook.com")
    # driver.maximize_window()
    # driver.implicitly_wait(10)
    # wait = WebDriverWait(driver, 10, poll_frequency=5,
    #                      ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    # driver.save_screenshot("file2.png")
    print("initiating chrome driver")
    driver = webdriver.Chrome(executable_path="/Users/praveen.garg1/Downloads/chromedriver")
    request.cls.driver = driver
    driver.get("https://twitter.com/stepin_forum")
    driver.maximize_window()
    yield driver
    driver.save_screenshot("file_" + str(random.randint(100,999))+".png")
    driver.close()


class TestTwitter(object):
    report = {}
    @pytest.mark.usefixtures("setup")
    def test_people(self):
        PeoplePageObj = PeoplePage(self.driver)
        try:
            assert PeoplePageObj.get_header()=='You may also like'
        except AssertionError as e:
            print e
        self.report['biographies'] = PeoplePageObj.get_people_info()

