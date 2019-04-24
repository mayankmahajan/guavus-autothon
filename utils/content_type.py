from enum import Enum


class ContentType(Enum):
    FORM_URLENCODED = "application/x-www-form-urlencoded; charset=UTF-8"
    APPLICATION_JSON = "application/json"