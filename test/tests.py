import unittest
from dict_update import dict_update

class TestDeepDictUpdate(unittest.TestCase):
    def test_dict_update_simple(self):
        orig_dict = {
            'a': {
                'b': 2,
                'c': {
                    'd': 3
                }
            }
        }

        new_dict = {
            'a': {
                'c': {
                    'e': 4
                },
                'f': 5
            },
            'g': 6
        }

        expected_result = {
            'a': {
                'b': 2,
                'c': {
                    'd': 3,
                    'e': 4
                },
                'f': 5
            },
            'g': 6
        }

        updated_dict = dict_update.dict_update(orig_dict, new_dict)
        self.assertEqual(updated_dict, expected_result)

    def test_dict_update_with_list(self):
        orig_dict = {
            'a': {
                'b': [1, 2, 3],
                'c': {
                    'd': 3
                }
            }
        }

        new_dict = {
            'a': {
                'b': [4, 5, 6],
                'c': {
                    'e': 4
                },
                'f': 5
            },
            'g': 6
        }

        expected_result = {
            'a': {
                'b': [4, 5, 6],
                'c': {
                    'd': 3,
                    'e': 4
                },
                'f': 5
            },
            'g': 6
        }

        updated_dict = dict_update.dict_update(orig_dict, new_dict)
        self.assertEqual(updated_dict, expected_result)

    def test_dict_update_with_objects_list(self):
        orig_dict = {
            'data': [
                {'id': 1, 'name': 'Alice'},
                {'id': 2, 'name': 'Bob'}
            ]
        }

        new_dict = {
            'data': [
                {'id': 3, 'name': 'Charlie'},
                {'id': 4, 'name': 'David'}
            ]
        }

        expected_result = {
            'data': [
                {'id': 3, 'name': 'Charlie'},
                {'id': 4, 'name': 'David'}
            ]
        }

        updated_dict = dict_update.dict_update(orig_dict, new_dict)
        self.assertEqual(updated_dict, expected_result)

    def test_dict_update_empty_orig_dict(self):
        orig_dict = {}

        new_dict = {
            'a': {
                'b': {
                    'c': 1
                }
            }
        }

        expected_result = {
            'a': {
                'b': {
                    'c': 1
                }
            }
        }

        updated_dict = dict_update.dict_update(orig_dict, new_dict)
        self.assertEqual(updated_dict, expected_result)

if __name__ == '__main__':
    unittest.main()
