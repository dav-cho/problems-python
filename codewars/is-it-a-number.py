##
#### Is it a number? (8 kyu)
################################


def isDigit(string):
    pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(isDigit("s2324"), False)
        self.assertEqual(isDigit("-234.4"), True)

        self.assertEqual(isDigit("3"), True)
        self.assertEqual(isDigit("  3  "), True)
        self.assertEqual(isDigit("-3.23"), True)
        self.assertEqual(isDigit("3-4"), False)
        self.assertEqual(isDigit("  3   5"), True)
        self.assertEqual(isDigit("3 5"), True)
        self.assertEqual(isDigit("zero"), True)
        self.assertEqual(isDigit("3 4"), False)


if __name__ == '__main__':
    unittest.main()

