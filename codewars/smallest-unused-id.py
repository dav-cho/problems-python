##
#### Smallest unused ID
###################################################

def next_id(arr):
    if not arr:
        return 0

    mx = max(arr) + 1
    hash = set(arr)
    for num in range(mx):
        if num not in hash:
            return num

    return mx


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEquals(next_id([0,1,2,3,4,5,6,7,8,9,10]), 11)
        self.assertEquals(next_id([5,4,3,2,1]), 0)
        self.assertEquals(next_id([0,1,2,3,5]), 4)
        self.assertEquals(next_id([0,0,0,0,0,0]), 1)
        self.assertEquals(next_id([]), 0)
        self.assertEquals(next_id([0,0,1,1,2,2]), 3)
        self.assertEquals(next_id([0,1,1,1,3,2]), 4)
        self.assertEquals(next_id([0,1,0,2,0,3]), 4)
        self.assertEquals(next_id([9,8,0,1,7,6]), 2)
        self.assertEquals(next_id([9,8,7,6,5,4]), 0)

if __name__ == '__main__':
    unittest.main()

