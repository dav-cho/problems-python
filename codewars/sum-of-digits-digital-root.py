##
#### Sum of Digits / Digital Root (6 kyu)
#############################################


def digital_root(n):
    digit_sum = sum(int(x) for x in str(n))

    while digit_sum > 9:
        digit_sum = digital_root(digit_sum)

    return digit_sum


def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))


def digital_root(n):
    return n % 9 or n and 9


## Tests
############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(digital_root(16), 7)
        self.assertEqual(digital_root(942), 6)
        self.assertEqual(digital_root(132189), 6)
        self.assertEqual(digital_root(493193), 2)


if __name__ == "__main__":
    unittest.main()

