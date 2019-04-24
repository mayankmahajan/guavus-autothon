import logging

import requests

from request_type import RequestType


# from nimble.core.utils.file_server_utils import FileServerUtils


class ApiRequest(object):
    def __init__(self):
        self._logger = logging.getLogger(__name__)

    @staticmethod
    def safe_extend(input_list, obj):
        if isinstance(obj, (dict, str, int)):
            input_list.append(obj)
        else:
            input_list.extend(obj)
        return input_list

    def execute_request(self, api_request_specification):
        """Execute the API request as per the request specification object.

        :type api_request_specification: :class:`nimble.core.api.api_request_specification.ApiRequestSpecification`
        :return: Response of the API request.
        :rtype: :class:`requests.Response`
        """
        request_type = api_request_specification.request_type
        self._logger.info(
            "Executing %s request with specification: %s" % (request_type, api_request_specification.__dict__))
        if request_type == RequestType.GET:
            response = requests.get(api_request_specification.url, params=api_request_specification.query_params,
                                    headers=api_request_specification.headers,
                                    timeout=api_request_specification.timeout, verify=api_request_specification.verify,
                                    auth=api_request_specification.auth)
        elif request_type == RequestType.POST:
            response = requests.post(api_request_specification.url, data=api_request_specification.data,
                                     json=api_request_specification.json, headers=api_request_specification.headers,
                                     params=api_request_specification.query_params,
                                     timeout=api_request_specification.timeout, files=api_request_specification.files,
                                     verify=api_request_specification.verify, auth=api_request_specification.auth)
        elif request_type == RequestType.PUT:
            response = requests.put(api_request_specification.url, data=api_request_specification.data,
                                    json=api_request_specification.json, headers=api_request_specification.headers,
                                    params=api_request_specification.query_params,
                                    timeout=api_request_specification.timeout, files=api_request_specification.files,
                                    verify=api_request_specification.verify, auth=api_request_specification.auth)
        elif request_type == RequestType.DELETE:
            response = requests.delete(api_request_specification.url, headers=api_request_specification.headers,
                                       timeout=api_request_specification.timeout,
                                       verify=api_request_specification.verify, auth=api_request_specification.auth)
        else:
            raise ValueError("Request type %s not supported" % request_type)
        if response.ok:
            self._logger.info("API Response code: %s" % response.status_code)
        else:
            self._logger.error(
                "API failed with status code:- %s\n%s" % (response.status_code, response.text))
        return response

    @staticmethod
    def validate_response_code(response, expected_code):
        return response.status_code == expected_code

    # def execute_multiple_requests(self, module_path, class_name, class_params, method_name, method_params,
    #                               payload_file=None, param_file=None):
    #     """Hit an API multiple times with the parameters given in payload and param file.
    #
    #     If the given `payload_file` and `param_file` are empty then the given method will be invoked with the
    #     `method_params` or else if above files are not empty then each row from payload and param file will be appended
    #     to the given `method_param` and then the method will get invoked for parameters in method parameters list.
    #
    #     :param module_path: Path of the file where user has defined the given class and method.
    #     :type module_path: str
    #     :param class_name: Name of the class which contains the given method.
    #     :type class_name: str
    #     :param class_params: Class parameters.
    #     :type class_params: list
    #     :param method_name: Name of the method that has to be invoked.
    #     :type method_name str
    #     :param method_params: Method parameters.
    #     :type method_params: list
    #     :param payload_file: Path of the payload file which contains the payloads. Defaults to `None`.
    #     :type payload_file: str
    #     :param param_file: Path of the param file which contains the parameters to be used in the API url. Defaults to
    #         `None`.
    #     :type param_file: str
    #     :return: Return list containing response of api for each parameter given in payload and param file.
    #     :rtype: list
    #     """
    #     response_list = []
    #     payload_list = []
    #     param_list = []
    #     file_server_utils = FileServerUtils()
    #     if payload_file:
    #         payload_list = self._populate_list(file_server_utils, payload_file)
    #     if param_file:
    #         param_list = self._populate_list(file_server_utils, param_file)
    #     try:
    #         class_obj = Helper.get_class_obj(module_path, class_name=class_name, class_parameters=class_params)
    #     except ConnectionError:
    #         self._logger.exception("Runtime exception while creating class object")
    #         return None
    #     length = max([len(payload_list), len(param_list)])
    #     if length == 0:
    #         response_list.append(
    #             Helper.call_method(method_name, class_obj=class_obj, method_parameters=method_params))
    #     else:
    #         if method_params is None:
    #             method_params = []
    #         for params in itertools.izip_longest(param_list, payload_list, fillvalue=[]):
    #             updated_method_params = []
    #             updated_method_params.extend(method_params)
    #             ApiRequest.safe_extend(updated_method_params, params[0])
    #             ApiRequest.safe_extend(updated_method_params, params[1])
    #             response_list.append(
    #                 Helper.call_method(method_name, class_obj=class_obj,
    #                                    method_parameters=updated_method_params))
    #     return response_list
    #
    # def _populate_list(self, file_server_utils, file_path):
    #     """Get a list populated with payloads provided in the given file `file_path`.
    #
    #     :type file_server_utils: :class:`nimble.core.utils.file_server_utils.FileServerUtils`
    #     :param file_path: Path to the file from which the payloads are to be extracted. This file can be present on
    #         local file system or can be placed on the file server.
    #     :type file_path: str
    #     :return: Return a list containing all the payloads.
    #     :rtype: list
    #     """
    #     if FileUtils.is_file(file_path):
    #         local_file_path = file_path
    #     else:
    #         self._logger.exception("File %s not present on local. Fetching from file server." % file_path)
    #         local_file_path = "%s/%s" % (global_constants.DEFAULT_LOCAL_TMP_PATH, file_path.split("/")[-1])
    #         file_server_utils.download(file_path)
    #     DynamicSubstitutionUtils.update_file(local_file_path)
    #     data_list = FileUtils.read_file_as_list(local_file_path)
    #     try:
    #         data_list = [json.loads(payload) for payload in data_list]
    #     except ValueError:
    #         data_list = [param.strip("\n").split(",") for param in data_list]
    #     return data_list
