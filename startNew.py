import json
import requests
import logging

my_file = open("test_python_qa.txt", "w")
logging.basicConfig(filename='log_test_python_qa.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('This is a log message.')

requestsArgs = {"test": "3", "test2": "two"}
resOne = requests.get('http://httpbin.org/get', requestsArgs)
parsed_string = json.loads(resOne.text)