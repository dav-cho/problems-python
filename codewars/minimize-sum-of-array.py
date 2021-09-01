##
#### Minimize Sum Of Array (Array Series #1) (7 kyu)
########################################################


def min_sum(arr):
    arr.sort()
    sum = 0
    for i in range(len(arr) // 2):
        sum += arr[i] * arr[-1 - i]

    return sum


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(min_sum([5,4,2,3]), 22)
        self.assertEqual(min_sum([12,6,10,26,3,24]), 342)
        self.assertEqual(min_sum([9,2,8,7,5,4,0,6]), 74)


if __name__ == '__main__':
    unittest.main()

