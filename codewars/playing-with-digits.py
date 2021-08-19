##
#### Playing with digits (6 kyu)
####################################


def dig_pow(n, p):
    powers = sum(x ** (p + i) for i, x in enumerate(map(int, str(n))))
    k = powers / n

    if k.is_integer():
        return k

    return -1


def dig_pow(n, p):
    powers = sum(x ** (p + i) for i, x in enumerate(map(int, str(n))))
    k = powers / n

    return k if not powers % n else -1


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(dig_pow(89, 1), 1)
        self.assertEqual(dig_pow(92, 1), -1)
        self.assertEqual(dig_pow(46288, 3), 51)


if __name__ == '__main__':
    unittest.main()

