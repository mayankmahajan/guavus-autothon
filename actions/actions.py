import logging

from utils.api_request import ApiRequest
from utils.api_request_specification import ApiRequestSpecification
from utils.request_type import RequestType


class Actions(object):
    def __init__(self, base_url, test_header):
        self._logger = logging.getLogger(__name__)
        # self.username = username
        # self.password = password
        self.base_url = base_url
        self.api_request = ApiRequest()
        # self.headers = {"test_header": test_header_value}
        self.headers = test_header
        self.verify = False

    # def login(self):
    #     url = "%s/session" % self.base_url
    #     payload = {"username": self.username, "password": self.password}
    #     api_request_specification = ApiRequestSpecification(RequestType.POST, url=url, headers=self.headers,
    #                                                         json=payload, verify=self.verify)
    #     token = self.api_request.execute_request(api_request_specification).json()["token"]
    #     self.headers["X-Cookie"] = "token=%s" % token

    def generate_request(self):
        url = "%s" % (self.base_url)
        api_request_specification = ApiRequestSpecification(RequestType.GET, url=url, headers=self.headers)
        return self.api_request.execute_request(api_request_specification)
