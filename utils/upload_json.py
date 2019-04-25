#
#
# import requests
# from utils.json_parser import JsonParser
#
# url = 'https://cgi-lib.berkeley.edu/ex/fup.html'
#
# # info = {
# #     'var1' : 'this',
# #     'var2'  : 'that',
# # }
#
#
# data = JsonParser.parse_json('/Users/mayank.mahajan/guavus-autothon/resources/json_output')
#
# headers = {'Content-type': 'multipart/form-data'}
#
# files = {'document': open('file_name.pdf', 'rb')}
#
# r = requests.post(url, files=files, data=data, headers=headers)
# pass
import json
import os
import requests
url = 'https://cgi-lib.berkeley.edu/ex/fup.html'

def send_request():
    payload = {"param_1": "value_1", "param_2": "value_2"}
    files = {
         'json': (None, json.dumps(payload), 'application/json')
    }

    r = requests.post(url, files=files)
    print(r.content)
    # r1 = requests.post("https://cgi-lib.berkeley.edu/ex/fup.cgi")

    # cmd = '''curl 'https://cgi-lib.berkeley.edu/ex/fup.cgi' -X POST -H 'Connection: keep-alive' -H 'Content-Length: 1259' -H 'Cache-Control: max-age=0' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36' -H 'Origin: https://cgi-lib.berkeley.edu' -H 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryG2hRW0iJhuXEvEL9' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' -H 'Referer: https://cgi-lib.berkeley.edu/ex/fup.html' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.9,de;q=0.8' --compressed'''

    # print os.system(cmd)
    # print(r1.content)

send_request()


# curl 'https://cgi-lib.berkeley.edu/ex/fup.cgi' -X POST -H 'Connection: keep-alive' -H 'Content-Length: 1259' -H 'Cache-Control: max-age=0' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36' -H 'Origin: https://cgi-lib.berkeley.edu' -H 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryG2hRW0iJhuXEvEL9' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' -H 'Referer: https://cgi-lib.berkeley.edu/ex/fup.html' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: en-US,en;q=0.9,de;q=0.8' --compressed

