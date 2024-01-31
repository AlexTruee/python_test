from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By

LOGIN = 'LOGIN'
PASSWORD = 'PASSWORD'


class TestYandexAuth(TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def test_yandex_aut(self):
        self.driver.get('https://passport.yandex.ru/auth/')
        self.driver.implicitly_wait(5)

        login_input = self.driver.find_element(By.NAME, 'login')
        self.driver.implicitly_wait(3)
        login_input.send_keys(LOGIN)
        login_input.submit()

        self.driver.implicitly_wait(5)

        password_input = self.driver.find_element(By.NAME, 'passwd')
        self.driver.implicitly_wait(3)
        password_input.send_keys(PASSWORD)
        password_input.submit()

        self.driver.implicitly_wait(5)

    def tearDown(self) -> None:
        self.driver.quit()
