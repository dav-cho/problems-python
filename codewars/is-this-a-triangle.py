##
#### Is this a triangle? (7 kyu)
####################################


def is_triangle(a, b, c,):
    p = (a + b + c) / 2
    A = (p * (p - a) * (p - b) * (p - c)) ** 0.5

    if a + b > c and a + c > b and b + c >= a and A:
        return True

    return False


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(is_triangle(1, 2, 2), True, "didn't work when sides were 1, 2, 2")
        self.assertEqual(is_triangle(7, 2, 2), False, "didn't work when sides were 7, 2, 2")
        self.assertEqual(is_triangle(1, 2, 3), False, "didn't work when sides were 1, 2, 3")
        self.assertEqual(is_triangle(1, 3, 2), False, "didn't work when sides were 1, 3, 2")
        self.assertEqual(is_triangle(3, 1, 2), False, "didn't work when sides were 3, 1, 2")
        self.assertEqual(is_triangle(5, 1, 2), False, "didn't work when sides were 5, 1, 2")
        self.assertEqual(is_triangle(1, 2, 5), False, "didn't work when sides were 1, 2, 5")
        self.assertEqual(is_triangle(2, 5, 1), False, "didn't work when sides were 2, 5, 1")
        self.assertEqual(is_triangle(4, 2, 3), True, "didn't work when sides were 4, 2, 3")
        self.assertEqual(is_triangle(5, 1, 5), True, "didn't work when sides were 5, 1, 5")
        self.assertEqual(is_triangle(2, 2, 2), True, "didn't work when sides were 2, 2, 2")
        self.assertEqual(is_triangle(-1, 2, 3), False, "didn't work when sides were -1, 2, 3")
        self.assertEqual(is_triangle(1, -2, 3), False, "didn't work when sides were 1, -2, 3")
        self.assertEqual(is_triangle(1, 2, -3), False, "didn't work when sides were 1, 2, -3")
        self.assertEqual(is_triangle(0, 2, 3), False, "didn't work when sides were 0, 2, 3")


if __name__ == '__main__':
    unittest.main()

