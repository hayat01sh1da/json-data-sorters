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
        self.directory = os.path.join('test', 'tmp')
        self.filepath  = os.path.join(self.directory, 'users.json')
        if not os.path.isdir(self.directory):
            os.makedirs(self.directory)
        with open(self.filepath, 'w') as f:
            f.write(self.__json_data__())

    ########## Regular Cases ##########

    def test_sort_json_data_by_asc(self):
        Application(filepath = self.filepath).run()
        self.assertEqual(self.__actual_json__(), self.__sorted_user_data_by_asc__())

    def test_sort_json_data_by_desc(self):
        Application(filepath = self.filepath, order = 'desc').run()
        self.assertEqual(self.__actual_json__(), self.__sorted_user_data_by_desc__())

    ########## Irregular Cases ##########

    def test_sort_json_data_with_invalid_order_type(self):
        with self.assertRaises(ValueError, msg = 'order option must be either asc or desc'):
            Application(filepath = self.filepath, order = 'hoge').run()

    def tearDown(self):
        if self.__has_json_file__():
            shutil.rmtree(self.directory)

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

    def __has_json_file__(self):
        return len(glob.glob(os.path.join(self.directory, '*.json'))) >= 1

if __name__ == '__main__':
    unittest.main()
