import unittest
import os
import glob
import shutil
import sys
sys.path.append('./src')
import json
from application import Application

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.dirname  = os.path.join('.', 'test', 'tmp')
        self.filename = 'users.json'
        self.filepath = os.path.join(self.dirname, self.filename)
        os.makedirs(self.dirname, exist_ok = True)
        with open(self.filepath, 'w') as f:
            f.write(self.__json_data__())
        self.pycaches = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)

    def tearDown(self):
        if os.path.exists(self.dirname):
            shutil.rmtree(self.dirname)
        for pycache in self.pycaches:
            if os.path.exists(pycache):
                shutil.rmtree(pycache)

    ########## Regular Cases ##########

    def test_sort_json_data_by_asc(self):
        Application(dirname = self.dirname, filename = self.filename).run()
        self.assertEqual(self.__actual_json__(), self.__sorted_user_data_by_asc__())

    def test_sort_json_data_by_desc(self):
        Application(dirname = self.dirname, filename = self.filename, order = 'desc').run()
        self.assertEqual(self.__actual_json__(), self.__sorted_user_data_by_desc__())

    ########## Irregular Cases ##########

    def test_sort_json_data_with_missing_filename(self):
        with self.assertRaises(ValueError) as cm:
            Application(dirname = self.dirname, filename = '').run()
        self.assertEqual('Filename must be provided.', str(cm.exception))

    def test_sort_json_data_with_invalid_order(self):
        with self.assertRaises(ValueError) as cm:
            Application(dirname = self.dirname, filename = self.filename, order = 'hoge').run()
        self.assertEqual('Order option must be either asc or desc.', str(cm.exception))

    def test_sort_json_data_with_non_string_order(self):
        with self.assertRaises(ValueError) as cm:
            Application(dirname = self.dirname, filename = self.filename, order = 1).run()
        self.assertEqual('Unexpected param was provided', str(cm.exception))

    # private

    # Conf. https://7esl.com/english-names/
    def __actual_json__(self):
        json_data = None
        with open(self.filepath) as f:
            json_data = json.load(f)
        return json_data

    def __json_data__(self):
        return json.dumps(self.__user_data__(), ensure_ascii = False, indent = 2)

    def __user_data__(self):
        return {
            'user2': {
                'name': 'Wade Williams',
                'age': 45,
                'gender': 'Male',
                'occupation': 'Global Trading Marketer',
                'skills': {
                    'languages': [
                        'Japanese',
                        'English',
                        'Spanish',
                        'German',
                        'French'
                    ],
                    'expertise': [
                        'Marketing',
                        'Accounting',
                        'Interpretation',
                        'Translation',
                        'Economics'
                    ]
                }
            },
            'user3': {
                'name': 'Daisy Harris',
                'age': 30,
                'gender': 'Female',
                'occupation': 'High School Teacher',
                'skills': {
                    'languages': [
                        'English',
                        'Spanish'
                    ],
                    'expertise': [
                        'Teaching Foreign Language'
                    ]
                }
            },
            'user1': {
                'name': 'Wade Williams',
                'age': 35,
                'occupation': 'Software Engineer',
                'skills': {
                    'languages': [
                        'Japanese',
                        'English'
                    ],
                    'expertise': [
                        'Server-Side Programming',
                        'Front-end Programming',
                        'Infrastructure Management',
                        'Team Members Management',
                    ]
                }
            }
        }

    def __sorted_user_data_by_asc__(self):
        return {
            'user1': {
                'age': 35,
                'name': 'Wade Williams',
                'occupation': 'Software Engineer',
                'skills': {
                    'languages': [
                        'Japanese',
                        'English'
                    ],
                    'expertise': [
                        'Server-Side Programming',
                        'Front-end Programming',
                        'Infrastructure Management',
                        'Team Members Management'
                    ]
                }
            },
            'user2': {
                'age': 45,
                'gender': 'Male',
                'name': 'Wade Williams',
                'occupation': 'Global Trading Marketer',
                'skills': {
                    'languages': [
                        'Japanese',
                        'English',
                        'Spanish',
                        'German',
                        'French'
                    ],
                    'expertise': [
                        'Marketing',
                        'Accounting',
                        'Interpretation',
                        'Translation',
                        'Economics'
                    ]
                }
            },
            'user3': {
                'age': 30,
                'gender': 'Female',
                'name': 'Daisy Harris',
                'occupation': 'High School Teacher',
                'skills': {
                    'languages': [
                        'English',
                        'Spanish'
                    ],
                    'expertise': [
                        'Teaching Foreign Language'
                    ]
                }
            }
        }

    def __sorted_user_data_by_desc__(self):
        return {
            'user3': {
                'skills': {
                    'languages': [
                        'English',
                        'Spanish'
                    ],
                    'expertise': [
                        'Teaching Foreign Language'
                    ]
                },
                'occupation': 'High School Teacher',
                'name': 'Daisy Harris',
                'gender': 'Female',
                'age': 30
            },
            'user2': {
                'skills': {
                    'languages': [
                        'Japanese',
                        'English',
                        'Spanish',
                        'German',
                        'French'
                    ],
                    'expertise': [
                        'Marketing',
                        'Accounting',
                        'Interpretation',
                        'Translation',
                        'Economics'
                    ]
                },
                'occupation': 'Global Trading Marketer',
                'name': 'Wade Williams',
                'gender': 'Male',
                'age': 45
            },
            'user1': {
                'skills': {
                    'languages': [
                        'Japanese',
                        'English'
                    ],
                    'expertise': [
                        'Server-Side Programming',
                        'Front-end Programming',
                        'Infrastructure Management',
                        'Team Members Management'
                    ]
                },
                'occupation': 'Software Engineer',
                'name': 'Wade Williams',
                'age': 35
            }
        }

if __name__ == '__main__':
    unittest.main()
