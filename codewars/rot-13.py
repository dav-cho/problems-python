##
#### Rot13
###################################################

def rot13(message):
    res = ''

    for char in message:
        if char.isalpha():
            old = ord(char)
            new = old + 13
            if 65 <= old <= 90:
                if new > 90:
                    new = new % 90 + 64
            if 97 <= old <= 122:
                if new > 122:
                    new = new % 122 + 96
            res += chr(new)
        else:
            res += char
            
    return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(rot13("test"),"grfg")
        self.assertEqual(rot13("Test"),"Grfg")


if __name__ == '__main__':
    unittest.main()

