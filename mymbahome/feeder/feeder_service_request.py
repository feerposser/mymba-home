import requests
from requests.exceptions import RequestException
from json.decoder import JSONDecodeError


class RequestFeeder:

    def __init__(self):
        self.url = "http://localhost:5000"

    def get_all_hotspots(self):
        objects = []
        try:
            url = self.url + "/hotspot/"
            response = requests.get(url=url)
            print(response.status_code)
            if response.status_code != 404:
                objects = response.json()
        except RequestException as re:
            print(re)
        except JSONDecodeError as je:
            print(je)
        finally:
            return objects

    def get_hostspot(self, resource):
        try:
            url = self.url + "/hotspot/{}/".format(resource)
            response = requests.get(url)
            print(response.status_code)
            if response.status_code != 404:
                return response.json()
        except RequestException as re:
            print(re)
        except JSONDecodeError as je:
            print(je)
        finally:
            pass