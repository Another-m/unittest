
import os
import unittest
from task_5_with_test.yandex_api import create_dir

URL = "https://cloud-api.yandex.net/v1/disk/resources"
token = '... '
name_dir = 'NewDir'

class ApiYandexDiskTest(unittest.TestCase):
    def test_add_dir(self):
        self.assertEqual(create_dir(token, name_dir, URL), 201)

    def test_add_dir_2(self):
        self.assertEqual(create_dir(token, name_dir, URL), 409)

    def test_add_dir_3(self):
        self.assertEqual(create_dir(token, 'dir_2', URL), 201)

    def test_add_dir_4(self):
        self.assertEqual(create_dir("000", name_dir, URL), 401)