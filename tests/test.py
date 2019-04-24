import json
import logging
import random

import pytest

from actions.actions import Actions
from utils.json_parser import JsonParser
from actions.login import LoginPage
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait

chromeOptions = webdriver.ChromeOptions()

@pytest.fixture(scope="class")
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
    driver.get("http://www.facebook.com")
    driver.maximize_window()
    yield driver
    driver.save_screenshot("file_" + str(random.randint(100,999))+".png")
    driver.close()

# ACTUAL_JSON_OBJ = """{"start":1554371401,"relations":[{"data":"dataset.default.customers.csv","program":"spark.default.joinerAttempt_2.phase-1","accesses":["read"],"runs":["8eb256f1-5785-11e9-b543-0242abe9b27"],"components":[]},{"data":"dataset.default.purchases.csv","program":"spark.default.joinerAttempt_1.phase-1","accesses":["read"],"runs":["e81f5601-5787-11e9-9f06-0242026a90e"],"components":[]},{"data":"dataset.default.customers.csv","program":"spark.default.joinerAttempt_2.phase-1","accesses":["read"],"runs":["e65a4a41-5783-11e9-b0c1-0242026aa90e"],"components":[]},{"data":"dataset.default.customers.csv","program":"spark.default.joinerAttempt_1.phase-1","accesses":["read"],"runs":["983396b1-5787-11e9-9090-0242abe9b297"],"components":[]},{"data":"dataset.default.Joiner_Dataset","program":"spark.default.joinerAttempt_2.phase-1","accesses":["write"],"runs":["e65a4a41-5783-11e9-b0c1-0242026aa90e"],"components":[]},{"data":"dataset.default.purchases.csv","program":"spark.default.joinerAttempt_2.phase-1","accesses":["read"],"runs":["e65a4a41-5783-11e9-b0c1-0242026aa90e"],"components":[]},{"data":"dataset.default.purchases.csv","program":"spark.default.joinerAttempt_2.phase-1","accesses":["read"],"runs":["8eb256f1-5785-11e9-b543-0242abe9b297"],"components":[]},{"data":"dataset.default.Joiner_Dataset","program":"spark.default.joinerAttempt_1.phase-1","accesses":["write"],"runs":["983396b1-5787-11e9-9090-0242abe9b297"],"components":[]},{"data":"dataset.default.purchases.csv","program":"spark.default.joinerAttempt_1.phase-1","accesses":["read"],"runs":["983396b1-5787-11e9-9090-0242abe9b297"],"components":[]},{"data":"dataset.default.Joiner_Dataset","program":"spark.default.joinerAttempt_2.phase-1","accesses":["write"],"runs":["8eb256f1-5785-11e9-b543-0242abe9b297"],"components":[]},{"data":"dataset.default.purchases.csv","program":"mapreduce.default.dummy_v1.phase-1","accesses":["read"],"runs":["05442791-56db-11e9-a2c0-024283865e4d"],"components":[]},{"data":"dataset.default.Joiner_Dataset","program":"spark.default.joinerAttempt_1.phase-1","accesses":["write"],"runs":["f488c8f1-5786-11e9-b20c-0242026aa90e"],"components":[]},{"data":"dataset.default.purchases.csv","program":"spark.default.joinerAttempt_1.phase-1","accesses":["read"],"runs":["f488c8f1-5786-11e9-b20c-0242026aa90e"],"components":[]},{"data":"dataset.default.customers.csv","program":"spark.default.joinerAttempt_1.phase-1","accesses":["read"],"runs":["e81f5601-5787-11e9-9f06-0242026aa90e"],"components":[]},{"data":"dataset.default.result","program":"mapreduce.default.dummy_v1.phase-1","accesses":["write"],"runs":["05442791-56db-11e9-a2c0-024283865e4d"],"components":[]},{"data":"dataset.default.Joiner_Dataset","program":"spark.default.joinerAttempt_1.phase-1","accesses":["write"],"runs":["e81f5601-5787-11e9-9f06-0242026aa90e"],"components":[]},{"data":"dataset.default.customers.csv","program":"spark.default.joinerAttempt_1.phase-1","accesses":["read"],"runs":["f488c8f1-5786-11e9-b20c-0242026aa90e"],"components":[]}],"programs":{"spark.default.joinerAttempt_1.phase-1":{"entityId":{"application":"joinerAttempt_1","version":"-SNAPSHOT","type":"Spark","program":"phase-1","namespace":"default","entity":"PROGRAM"}},"spark.default.joinerAttempt_2.phase-1":{"entityId":{"application":"joinerAttempt_2","version":"-SNAPSHOT","type":"Spark","program":"phase-1","namespace":"default","entity":"PROGRAM"}},"mapreduce.default.dummy_v1.phase-1":{"entityId":{"application":"dummy_v1","version":"-SNAPSHOT","type":"Mapreduce","program":"phase-1","namespace":"default","entity":"PROGRAM"}}},"data":{"dataset.default.result":{"entityId":{"dataset":"result","namespace":"default","entity":"DATASET"}},"dataset.default.customers.csv":{"entityId":{"dataset":"customers.csv","namespace":"default","entity":"DATASET"}},"dataset.default.purchases.csv":{"entityId":{"dataset":"purchases.csv","namespace":"default","entity":"DATASET"}},"dataset.default.Joiner_Dataset":{"entityId":{"dataset":"Joiner_Dataset","namespace":"default","entity":"DATASET"}}}}"""
# EXPECTED_JSON_OBJ = """{"start1":1371401, "end":1554457806, "start":155437141,"relations":[{"data":"dataset.default.customers.csv","program":"spark.default.joinerAttempt_2.phase-1","accesses":["read"],"runs":["8eb256f1-5785-11e9-b543-0242abe9b27"],"components":[]},{"data":"dataset.default.purchases.csv","program":"spark.default.joinerAttempt_1.phase-1","accesses":["read"],"runs":["e81f5601-5787-11e9-9f06-0242026a90e"],"components":[]},{"data":"dataset.default.customers.csv","program":"spark.default.joinerAttempt_2.phase-1","accesses":["read"],"runs":["e65a4a41-5783-11e9-b0c1-0242026aa90e"],"components":[]},{"data":"dataset.default.customers.csv","program":"spark.default.joinerAttempt_1.phase-1","accesses":["read"],"runs":["983396b1-5787-11e9-9090-0242abe9b297"],"components":[]},{"data":"dataset.default.Joiner_Dataset","program":"spark.default.joinerAttempt_2.phase-1","accesses":["write"],"runs":["e65a4a41-5783-11e9-b0c1-0242026aa90e"],"components":[]},{"data":"dataset.default.purchases.csv","program":"spark.default.joinerAttempt_2.phase-1","accesses":["read"],"runs":["e65a4a41-5783-11e9-b0c1-0242026aa90e"],"components":[]},{"data":"dataset.default.purchases.csv","program":"spark.default.joinerAttempt_2.phase-1","accesses":["read"],"runs":["8eb256f1-5785-11e9-b543-0242abe9b297"],"components":[]},{"data":"dataset.default.Joiner_Dataset","program":"spark.default.joinerAttempt_1.phase-1","accesses":["write"],"runs":["983396b1-5787-11e9-9090-0242abe9b297"],"components":[]},{"data":"dataset.default.purchases.csv","program":"spark.default.joinerAttempt_1.phase-1","accesses":["read"],"runs":["983396b1-5787-11e9-9090-0242abe9b297"],"components":[]},{"data":"dataset.default.Joiner_Dataset","program":"spark.default.joinerAttempt_2.phase-1","accesses":["write"],"runs":["8eb256f1-5785-11e9-b543-0242abe9b297"],"components":[]},{"data":"dataset.default.purchases.csv","program":"mapreduce.default.dummy_v1.phase-1","accesses":["read"],"runs":["05442791-56db-11e9-a2c0-024283865e4d"],"components":[]},{"data":"dataset.default.Joiner_Dataset","program":"spark.default.joinerAttempt_1.phase-1","accesses":["write"],"runs":["f488c8f1-5786-11e9-b20c-0242026aa90e"],"components":[]},{"data":"dataset.default.purchases.csv","program":"spark.default.joinerAttempt_1.phase-1","accesses":["read"],"runs":["f488c8f1-5786-11e9-b20c-0242026aa90e"],"components":[]},{"data":"dataset.default.customers.csv","program":"spark.default.joinerAttempt_1.phase-1","accesses":["read"],"runs":["e81f5601-5787-11e9-9f06-0242026aa90e"],"components":[]},{"data":"dataset.default.result","program":"mapreduce.default.dummy_v1.phase-1","accesses":["write"],"runs":["05442791-56db-11e9-a2c0-024283865e4d"],"components":[]},{"data":"dataset.default.Joiner_Dataset","program":"spark.default.joinerAttempt_1.phase-1","accesses":["write"],"runs":["e81f5601-5787-11e9-9f06-0242026aa90e"],"components":[]},{"data":"dataset.default.customers.csv","program":"spark.default.joinerAttempt_1.phase-1","accesses":["read"],"runs":["f488c8f1-5786-11e9-b20c-0242026aa90e"],"components":[]}],"programs":{"spark.default.joinerAttempt_1.phase-1":{"entityId":{"application":"joinerAttempt_1","version":"-SNAPSHOT","type":"Spark","program":"phase-1","namespace":"default","entity":"PROGRAM"}},"spark.default.joinerAttempt_2.phase-1":{"entityId":{"application":"joinerAttempt_2","version":"-SNAPSHOT","type":"Spark","program":"phase-1","namespace":"default","entity":"PROGRAM"}},"mapreduce.default.dummy_v1.phase-1":{"entityId":{"application":"dummy_v1","version":"-SNAPSHOT","type":"Mapreduce","program":"phase-1","namespace":"default","entity":"PROGRAM"}}},"data":{"dataset.default.result":{"entityId":{"dataset":"result","namespace":"default","entity":"DATASET"}},"dataset.default.customers.csv":{"entityId":{"dataset":"customers.csv","namespace":"default","entity":"DATASET"}},"dataset.default.purchases.csv":{"entityId":{"dataset":"purchases.csv","namespace":"default","entity":"DATASET"}},"dataset.default.Joiner_Dataset":{"entityId":{"dataset":"Joiner_Dataset","namespace":"default","entity":"DATASET"}}}}"""


## Sample test class with test method.

'''class TestApi(object):
    _logger = logging.getLogger(__name__)
    proxy_server_base_url = "http://192.168.134.195:1338"
    # test_header = {"X-ZINFO": "55556420:EzFOyd0zB6KmquoEAoxT1Q==", "X-VID": "CHRXNCLH0111",
    #                "X-AUTH": '{"mdn": "8436012163", "iat": "1550774158", "imsi": "311480420643009", "am": "pp", "des_ip":"2600:40ff:fff8:1:1:1:0:33:22790", "vsep_id": "CHRXNCLH0111", "src_ip": "2600:1004:b031:9979:6d84:cfa5:c861:4b31:38246"}',
    #                "X-Forwarded-For": "2600:1004:b031:9979:6d84:cfa5:c861:4b31", "X-Forwarded-Port": "38246"}
    test_header = {
        "X-AUTH": '{"mdn": "8436012163", "iat": "1550774158", "imsi": "311480420643009", "am": "pp", "des_ip":"2600:40ff:fff8:1:1:1:0:33:22790", "vsep_id": "CHRXNCLH0111", "src_ip": "2600:1004:b031:9979:6d84:cfa5:c861:4b31:38246"}',
        "X-Forwarded-For": "2600:1004:b031:9979:6d84:cfa5:c861:4b31", "X-Forwarded-Port": "38246"}

    @pytest.fixture(scope="session")
    def actions(self):
        return Actions(base_url=self.proxy_server_base_url, test_header=self.test_header).generate_request()

    def test_1(self, actions):
        assert str(json.loads(actions._content)['x-st']) == "PB"

    def test_2(self):
        response = JsonParser.json_diff(json.loads(ACTUAL_JSON_OBJ), json.loads(EXPECTED_JSON_OBJ),
                                        ignore=set(['start', 'end', 'start1']))
        print response
'''

## dependent and independent test cases

'''
import pytest



class TestClass(object):

    @pytest.mark.dependency()
    @pytest.mark.xfail(reason="deliberate fail")
    def test_a(self):
        assert False

    @pytest.mark.dependency()
    def test_b(self):
        pass

    @pytest.mark.dependency(depends=["TestClass::test_a"])
    def test_c(self):
        pass

    @pytest.mark.dependency(depends=["TestClass::test_b"])
    def test_d(self):
        pass

    @pytest.mark.dependency(depends=["TestClass::test_b", "TestClass::test_c"])
    def test_e(self):
        pass
'''

## sample selenium test cases

'''
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


@pytest.fixture(scope="class")
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(executable_path="/Users/praveen.garg1/Downloads/chromedriver")
    request.cls.driver = driver
    driver.get("http://seleniumeasy.com/test")
    driver.maximize_window()

    yield driver
    driver.close()


@pytest.mark.usefixtures("setup")
class TestExample:

    @pytest.mark.smoke
    def test_title(self):
        print("Verify title...")
        assert "Selenium Easy" in self.driver.title

    @pytest.mark.smoke
    def test_content_text(self):
        print("Verify content on the page...")
        centertext = self.driver.find_element_by_css_selector('.tab-content .text-center').text
        assert "WELCOME TO SELENIUM EASY DEMO" == centertext

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_practicing(self):
        print("verifying exercise--")
        startpractisingBtn = self.driver.find_element_by_id('btn_basic_example')
        startpractisingBtn.click()
        time.sleep(10)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#basic .head')))
'''
@pytest.mark.usefixtures("setup")
class TestLogin(object):
    def test_login(self):
        assert LoginPage().login(self.driver)==True