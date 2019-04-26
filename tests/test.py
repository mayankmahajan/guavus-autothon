import json
import logging
import os
import platform
import random

import allure
import pytest
import requests
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import actions.globals as gbl
from utils.Tweet import Tweet
from utils.people import PeoplePage

chromeOptions = webdriver.ChromeOptions()
url = os.environ["URL"]
server_url = os.environ["Server_URL"]
logger = logging.getLogger(__name__)


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
    chromeOptions.binary_location = __binary_location()
    driver = webdriver.Chrome(executable_path=os.path.join(os.getcwd(), "resources", "chromedriver"),
                              options=chromeOptions)
    request.cls.driver = driver
    driver.get(url)
    driver.maximize_window()
    driver.set_page_load_timeout(30)
    wait = WebDriverWait(driver, 10, poll_frequency=5,
                         ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    element = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@class='js-nav js-tooltip js-dynamic-tooltip']//span[@class='Icon Icon--bird Icon--large']")))
    with allure.step("test_url"):
        assert get_url(driver) == str(url)

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
            with allure.step("test_title"):
                allure.attach(str(get_title(self.driver)), name="Actual_title", attachment_type=AttachmentType.TEXT)
                allure.attach(str('STeP-IN Forum (@stepin_forum) on Twitter'), name="Expected_title",
                              attachment_type=AttachmentType.TEXT)
                logger.info("Actual Title: %s" % str(get_title(self.driver)))
                logger.info("Expetced Title: %s" % str('STeP-IN Forum (@stepin_forum) on Twitter'))
                assert get_title(self.driver) == 'STeP-IN Forum (@stepin_forum) on Twitter'
        except AssertionError as e:
            print e

        gbl.my_data['biographies'] = PeoplePageObj.get_people_info()
        logger.info("People details : %s" % str(gbl.my_data['biographies']))
        with allure.step("number_of_people"):
            assert len(gbl.my_data['biographies']) > 0

    @pytest.mark.usefixtures("setup")
    def test_top_retweet(self):
        TweetPageObj = Tweet(self.driver, url)
        reTweetList = TweetPageObj.get_retweets()
        logger.info("Top retweet count list: %s" % str(reTweetList))
        gbl.my_data['top_retweet_count'] = max(reTweetList)
        logger.info("Top Retweet Count: %s" % str(gbl.my_data['top_retweet_count']))
        with allure.step("number_of_retweet"):
            assert len(reTweetList) > 0

    @pytest.mark.usefixtures("setup")
    def test_top_like(self):
        TweetPageObj = Tweet(self.driver, url)
        likes = TweetPageObj.get_likes()
        logger.info("Top likes count list: %s" % str(likes))
        gbl.my_data['top_like_count'] = max(likes)
        logger.info("Top Like Count: %s" % str(gbl.my_data['top_like_count']))
        with allure.step("number_of_likes"):
            assert len(likes) > 0

    @pytest.mark.usefixtures("setup")
    def test_top_hashtags(self):
        TweetPageObj = Tweet(self.driver, url)
        gbl.my_data['top_10_hashtags'] = TweetPageObj.get_top_n_hashtags(10)
        logger.info("Top 10 HashTags: %s" % str(gbl.my_data['top_10_hashtags']))
        with allure.step("number_of_hashtags"):
            assert len(gbl.my_data['top_10_hashtags']) > 0

    def test_send_file_to_server(self):
        url = str(server_url)
        files = {
            'json': (None, dict_to_json(gbl.my_data), 'application/json')
        }

        allure.attach(str(gbl.my_data), name="uploaded_json", attachment_type=AttachmentType.TEXT)
        r = requests.post(url, files=files)

        with allure.step("test_send_file"):
            assert int(r.status_code) == 200
