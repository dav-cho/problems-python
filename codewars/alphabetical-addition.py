##
#### Alphabetical Addition (7 kyu)
######################################


def add_letters(*letters):
    codex = {}
    for i in range(97, 97 + 26):
        codex[chr(i)] = i - 96

    result = sum(codex[letter] for letter in letters) % 26

    return chr(result + 96) if result > 0 else 'z'


def add_letters(*letters):
    result = sum(ord(letter) - 96 for letter in letters) % 26

    return chr(result + 96) if result > 0 else 'z'


def add_letters(*letters):
    return chr((sum(ord(c) - 96 for c in letters) - 1) % 26 + 97)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        tests = [
                (['a', 'b', 'c'], 'f'),
                (['z'], 'z'),
                (['a', 'b'], 'c'),
                (['c'], 'c'),
                (['z', 'a'], 'a'),
                (['y', 'c', 'b'], 'd'),
                ([], 'z')
                ]

        for test in tests:
            self.assertEqual(add_letters(*test[0]), test[1])


if __name__ == '__main__':
    unittest.main()

