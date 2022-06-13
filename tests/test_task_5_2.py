import unittest
from task_5_with_test.task_5_2 import search_data, add_data, delete_doc



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.comm = ''
        self.num_doc = ''
        self.test_data = {"command": None, "mum_doc": None, "doc_unique": None, "type_doc": None, "name": None, "num_shelf": None, "shelf_unique": None, "status": None}

    # def tearDown(self):
    #     print("method tearDown")

    def test_search_data(self):
        self.test_data['command'] = 'p'
        self.test_data['mum_doc'] = "11-2"
        self.assertEqual(search_data(self.test_data), result_p)

    def test_add_data(self):
        self.test_data['command'] = 'a'
        self.test_data['mum_doc'] = "11-2"
        self.assertEqual(add_data(self.test_data), result_a)

    def test_delete_doc(self):
        self.test_data['command'] = 'd'
        self.test_data['mum_doc'] = "10006"
        self.assertEqual(delete_doc(self.test_data), result_d)

result_p = 'Геннадий Покемонов'
result_a = 'документ 11-2 уже существует!'
result_d = 'Документ удален'



if __name__ == '__main__':
    unittest.main()
