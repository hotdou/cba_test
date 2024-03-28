from helpers.logger import get_global_logger
import requests
from urllib3.exceptions import HTTPError

logger = get_global_logger(__name__)

class HTTPClient:
    @classmethod
    def get(cls, url, headers=None, params=None, timeout=10):
        logger.info(f"GET URL => {url}")
        logger.info(f"GET HEADERS => {headers}")
        res = requests.get(
            url, headers=headers, params=params, timeout=timeout, verify=True
        )
        logger.info(f"GET RESPONSE => {res}")
        return res

    @classmethod
    def post(cls, url, a_dict=None, data=None, files=None, headers=None, timeout=10):
        logger.info(f"POST URL => {url}")
        logger.info(f"POST HEADERS => {headers}")
        logger.info(f"POST JSON => {a_dict}")
        logger.info(f"POST FORM DATA => {data}")
        logger.info(f"POST FILES => {files}")
        res = requests.post(
            url, json=a_dict, data=data, files=files, headers=headers, timeout=timeout, verify=True
        )
        logger.info(f"POST RESPONSE => {res}")
        return res

    @classmethod
    def put(cls, url, a_dict, headers=None, timeout=10):
        logger.info(f"PUT URL => {url}")
        logger.info(f"PUT HEADERS => {headers}")
        logger.info(f"PUT BODY => {a_dict}")
        res = requests.put(
            url, json=a_dict, headers=headers, timeout=timeout, verify=True
        )
        logger.info(f"PUT RESPONSE => {res}")
        return res

    @classmethod
    def delete(cls, url, a_dict=None, headers=None, timeout=10, params=None):
        logger.info(f"DELETE URL => {url}")
        logger.info(f"DELETE HEADERS => {headers}")
        logger.info(f"DELETE BODY => {a_dict}")
        res = requests.delete(
            url,
            json=a_dict,
            headers=headers,
            timeout=timeout,
            verify=True,
            params=params,
        )
        logger.info(f"DELETE RESPONSE => {res}")
        return res