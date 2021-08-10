##
#### Simple validation of a username with regex
###################################################

import re


def validate_user(username):
    pattern = re.compile('[a-z0-9_]{4,16}')
    result = pattern.fullmatch(username)

    return result != None


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(validate_user('asddsa'), True)
        self.assertEqual(validate_user('a'), False)
        self.assertEqual(validate_user('Hass'), False)
        self.assertEqual(validate_user('Hasd_12assssssasasasasasaasasasasas'), False)
        self.assertEqual(validate_user(''), False)
        self.assertEqual(validate_user('____'), True)
        self.assertEqual(validate_user('012'), False)
        self.assertEqual(validate_user('p1pp1'), True)
        self.assertEqual(validate_user('asd43 34'), False)
        self.assertEqual(validate_user('asd43_34'), True)


if __name__ == '__main__':
    unittest.main()

