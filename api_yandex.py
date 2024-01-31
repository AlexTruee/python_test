import requests
import os
import json


class YandexDisk:
    def __init__(self, access_token_yd: str):
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources'
        self.access_token_yd = access_token_yd

    def get_headers(self):
        headers = {
            'Content-type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.access_token_yd)
        }
        return headers

    def create_folder(self, name_folder):
        headers = self.get_headers()
        params = {"path": name_folder, "url": self.url}
        response = requests.put(self.url, headers=headers, params=params)

        return response.status_code

    def get_folder_info(self, name_folder):
        headers = self.get_headers()
        params = {'path': name_folder}
        response = requests.get(self.url, headers=headers, params=params)
        if response.status_code == 200:
            result_dict = json.loads(response.text)
            return result_dict.get('type')

    def del_folder(self, name_folder):
        headers = self.get_headers()
        params = {'path': name_folder, }
        response = requests.delete(self.url, headers=headers, params=params)
        return response.status_code
