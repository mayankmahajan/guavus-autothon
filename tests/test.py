import json
import os
import platform
import random

import allure
import pytest
import requests
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import actions.globals as gbl
from utils.Tweet import Tweet
from utils.people import PeoplePage

chromeOptions = webdriver.ChromeOptions()


def dict_to_json(dict):
    return json.dumps(dict)


def get_url(driver):
    return driver.current_url


def get_title(driver):
    return driver.title

def __binary_location():
    """This will work only for Darwin and Linux platforms."""
    if platform.system() == "Darwin":
        return "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    elif platform.system() == "Linux":
        return "/usr/bin/google-chrome"

@pytest.fixture(scope="function")
def setup(request):
    print("initiating chrome driver")
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('--headless')
    chromeOptions.add_argument('--no-sandbox')
    chromeOptions.binary_location=__binary_location()
    print("initiating chrome driver")
    driver = webdriver.Chrome(executable_path=os.path.join(os.getcwd(),"resources","chromedriver"),options=chromeOptions)
    request.cls.driver = driver
    driver.get("https://twitter.com/stepin_forum")
    driver.maximize_window()
    driver.set_page_load_timeout(30)
    wait = WebDriverWait(driver, 10, poll_frequency=5,
                         ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    element = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@class='js-nav js-tooltip js-dynamic-tooltip']//span[@class='Icon Icon--bird Icon--large']")))
    with allure.step("test_title"):
        assert get_title(driver) == 'STeP-IN Forum (@stepin_forum) on Twitter'

    with allure.step("test_url"):
        assert get_url(driver) == 'https://twitter.com/stepin_forum'

    yield driver
    driver.save_screenshot("file_" + str(random.randint(100, 999)) + ".png")
    driver.close()


class TestTwitter(object):
    @pytest.mark.usefixtures("setup")
    def test_people(self):
        PeoplePageObj = PeoplePage(self.driver)
        try:
            with allure.step("test_header"):
                assert PeoplePageObj.get_header() == 'You may also like'
        except AssertionError as e:
            print e
        gbl.my_data['biographies'] = PeoplePageObj.get_people_info()
        with allure.step("number_of_people"):
            assert len(gbl.my_data['biographies']) > 0

    @pytest.mark.usefixtures("setup")
    def test_retweet(self):
        TweetPageObj = Tweet(self.driver)
        reTweetList = TweetPageObj.get_retweets()
        gbl.my_data['top_retweet_count'] = max(reTweetList)
        with allure.step("number_of_retweet"):
            assert len(reTweetList) > 0

    @pytest.mark.usefixtures("setup")
    def test_top_like(self):
        TweetPageObj = Tweet(self.driver)
        likes= TweetPageObj.get_likes()
        gbl.my_data['top_like_count'] = max(likes)
        with allure.step("number_of_likes"):
            assert len(likes) > 0

    @pytest.mark.usefixtures("setup")
    def test_top_hashtags(self):
        TweetPageObj = Tweet(self.driver)
        gbl.my_data['top_10_hashtags'] = TweetPageObj.get_top_n_hashtags(10)
        with allure.step("number_of_hashtags"):
            assert len(gbl.my_data['top_10_hashtags']) > 0

    def test_send_to_server(self):
        url = 'https://cgi-lib.berkeley.edu/ex/fup.html'
        files = {
            'json': (None, dict_to_json(gbl.my_data), 'application/json')
        }
        r = requests.post(url, files=files)

        with allure.step("test_send_file"):
            assert int(r.status_code) == 200
