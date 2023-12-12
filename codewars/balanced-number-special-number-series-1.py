##
#### Balanced Number (Special Numbers Series #1 ) (7 kyu)
#############################################################


def balanced_num(number):
    num = str(number)
    length = len(num)

    left = right = 0
    if length % 2:
        mid = len(num) // 2
        left = sum(int(num[i]) for i in range(mid))
        right = sum(int(num[i]) for i in range(mid + 1, len(num)))
    else:
        mid = len(num) // 2
        left = sum(int(num[i]) for i in range(mid - 1))
        right = sum(int(num[i]) for i in range(mid + 1, len(num)))
        
    return 'Balanced' if left == right else 'Not Balanced'


def balanced_num(number):
    num = str(number)
    mid = (len(num) - 1) // 2
    left = sum(map(int, num[:mid]))
    right = sum(map(int, num[-mid:]))
    res = len(num) < 3 or left == right

    return 'Balanced' if res else 'Not Balanced'


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(balanced_num(7)  , "Balanced")
        self.assertEqual(balanced_num(959), "Balanced")
        self.assertEqual(balanced_num(13) , "Balanced")
        self.assertEqual(balanced_num(432), "Not Balanced")
        self.assertEqual(balanced_num(424), "Balanced")
        self.assertEqual(balanced_num(1024)    , "Not Balanced")
        self.assertEqual(balanced_num(66545)   , "Not Balanced")
        self.assertEqual(balanced_num(295591)  , "Not Balanced")
        self.assertEqual(balanced_num(1230987) , "Not Balanced")
        self.assertEqual(balanced_num(56239814), "Balanced")


if __name__ == '__main__':
    unittest.main()

