import os
from unittest import TestCase

import requests
from dotenv import load_dotenv, find_dotenv

from api_yandex import YandexDisk

load_dotenv(find_dotenv())

FOLDERNAME = 'TEST_FOLDER9'


class TestYandex(TestCase):
    @classmethod
    def setUp(cls):
        cls.yd = YandexDisk(os.getenv('ACCESS_TOKEN_YD'))

    def test_create_folder_201(self):
        result = self.yd.create_folder(FOLDERNAME)
        self.assertEqual(result, 201, f'Сервер ответил: {result}')

    def test_no_authorization_401(self):
        headers = self.yd.get_headers()
        headers.pop('Authorization')

        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {"path": FOLDERNAME, "url": url}
        response = requests.put(url, headers=headers, params=params)

        self.assertEqual(response.status_code, 401, f'Сервер ответил: {response.status_code}')

    def test_no_resource_404(self):
        result = self.yd.create_folder('//' + FOLDERNAME)
        self.assertEqual(result, 404, f'Сервер ответил: {result}')

    def test_create_folder_409(self):

        self.assertEqual(self.yd.create_folder(FOLDERNAME), 409, "Папка еще не создана")

    def test_get_folder_info(self):
        try:
            self.assertTrue(self.yd.get_folder_info(FOLDERNAME) == 'dir')
            print('Папка расположена на сервере')
        except AssertionError as e:
            print(f'Папка еще не создана. Ответ сервера:{e}')

    def test_get_folder_info_400(self):
        self.assertFalse(self.yd.get_folder_info(FOLDERNAME + '1') == 'dir')

    # def test_del_folder(self):
    #     self.assertEqual(self.yd.del_folder(FOLDERNAME), 204)
