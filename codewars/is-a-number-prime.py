##
#### Is a number prime? (6 kyu)
###################################################


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if not num % 2:
        return False

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
        
    return True


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(is_prime(0),  False, "0  is not prime")
        self.assertEqual(is_prime(1),  False, "1  is not prime")
        self.assertEqual(is_prime(2),  True, "2  is prime")
        self.assertEqual(is_prime(73), True, "73 is prime")
        self.assertEqual(is_prime(75), False, "75 is not prime")
        self.assertEqual(is_prime(-1), False, "-1 is not prime")
        self.assertEqual(is_prime(3),  True, "3  is prime");
        self.assertEqual(is_prime(5),  True, "5  is prime");
        self.assertEqual(is_prime(7),  True, "7  is prime");
        self.assertEqual(is_prime(41), True, "41 is prime");
        self.assertEqual(is_prime(5099), True, "5099 is prime");
        self.assertEqual(is_prime(4),  False, "4  is not prime");
        self.assertEqual(is_prime(6),  False, "6  is not prime");
        self.assertEqual(is_prime(8),  False, "8  is not prime");
        self.assertEqual(is_prime(9), False, "9 is not prime");
        self.assertEqual(is_prime(45), False, "45 is not prime");
        self.assertEqual(is_prime(-5), False, "-5 is not prime");
        self.assertEqual(is_prime(-8), False, "-8 is not prime");
        self.assertEqual(is_prime(-41), False, "-41 is not prime");


if __name__ == '__main__':
    unittest.main()

