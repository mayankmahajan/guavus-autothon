import json
import logging
from collections import OrderedDict

from dictdiffer import diff
from flatten_dict import flatten

# from nimble.core.utils.collection_utils import CollectionUtils
# from nimble.core.utils.file_utils import FileUtils

_LOGGER = logging.getLogger(__name__)


class JsonParser(object):
    def __init__(self):
        pass

    @staticmethod
    def parse_json(file_path):
        with open(file_path) as f:
            return json.load(f)



    @staticmethod
    def parse_json_file_ordered(file_path):
        with open(file_path) as f:
            return json.load(f, object_pairs_hook=OrderedDict)

    @staticmethod
    def dump_json(file_path, dictionary):
        with open(file_path, "w+") as f:
            json.dump(dictionary, f, indent=4)


    @staticmethod
    def json_diff(old, new, **kwargs):
        """Json diff is used to take diff of two json objects.

        :param old: First json object which has to be compared with new json.
        :type old: dict
        :param new: Second json object which has to be compared with old json.
        :type new: dict
        :param kwargs: Keyword arguments to be passed to :class:`dictdiffer.Diff()` function.
        :type kwargs: dict
        :return: Return diff of two json objects.
        :rtype: list
        """
        old_obj = flatten(old)
        new_obj = flatten(new)
        return list(diff(old_obj, new_obj, **kwargs))
