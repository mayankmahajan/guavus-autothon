import os
import random

import allure
import pytest
import json
import requests
from selenium import webdriver

from utils.Tweet import Tweet
from utils.parser import ObjectRepository
from utils.people import PeoplePage

chromeOptions = webdriver.ChromeOptions()

@pytest.fixture(scope="function")
def setup(request):
    print("initiating chrome driver")
    chromeOptions.add_argument('--headless')
    chromeOptions.add_argument('--no-sandbox')
    # driver = webdriver.Remote(
    #     command_executor='http://192.168.135.96:4444/wd/hub', desired_capabilities=chromeOptions.to_capabilities())
    # driver.get("http://www.facebook.com")
    # driver.maximize_window()
    # driver.implicitly_wait(10)
    # wait = WebDriverWait(driver, 10, poll_frequency=5,
    #                      ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
    # driver.save_screenshot("file2.png")
    print("initiating chrome driver")
    driver = webdriver.Chrome(executable_path="/Users/anubhav.gupta/Downloads/chromedriver")
    request.cls.driver = driver
    driver.get("https://twitter.com/stepin_forum")
    driver.maximize_window()
    yield driver
    driver.save_screenshot("file_" + str(random.randint(100,999))+".png")
    driver.close()


class TestTwitter(object):
    report= {}
    locator = ObjectRepository(file_path=os.path.join(os.getcwd(), "actions", "tweet.csv"))
    @pytest.mark.usefixtures("setup")
    def test_tweet(self):
        PeoplePageObj = PeoplePage(self.driver)
        try:
            with allure.step("test_title"):
                assert PeoplePageObj.get_header()=='You may also like'
        except AssertionError as e:
            print e
        self.report['biographies'] = PeoplePageObj.get_people_info()
        self.report['top_retweet_count'] = max(Tweet(self.driver).get_retweets(self.locator.get_value('retweet')))
        self.report['top_like_count'] = max(Tweet(self.driver).get_likes(self.locator.get_value('likes')))
        self.report['top_10_hashtags'] = Tweet(self.driver).get_top_n_hashtags(10, locator=self.locator.get_value('hastags'))
        url = 'https://cgi-lib.berkeley.edu/ex/fup.html'

        files = {
                'json': (None, json.dumps(json.dumps(self.report)), 'application/json')
             }

        r = requests.post(url, files=files)
        with allure.step("test_title"):
            assert int(r.status_code)==200
