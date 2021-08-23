##
#### Maximum subarray sum (5 kyu)
#####################################


def max_sequence(arr):
    mx = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            mx = max(mx, sum(arr[i:i + j + 1]))
            
    return mx


def max_sequence(arr):
    mx = curr = 0
    for num in arr:
        curr += num
        
        if curr < 0:
            curr = 0
        if curr > mx:
            mx = curr
            
    return mx


def max_sequence(arr):
    if all(arr.filter(lambda x: x < 0, arr)):
        return 0

    mx = 0
    left = right = 0
    #prev = float('inf')
    while right < len(arr):
        curr = sum(arr[left:right])


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(max_sequence([]), 0)
        self.assertEqual(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]), 155)


if __name__ == '__main__':
    unittest.main()

