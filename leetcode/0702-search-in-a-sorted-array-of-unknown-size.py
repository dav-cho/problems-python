##
#### 702. Search in a Sorted Array of Unknown Size (medium)
###############################################################


## binary search
##############################
class Solution:
    def search(self, reader: "ArrayReader", target: int) -> int:
        if reader.get(0) == target:
            return 0

        left, right = 0, 1

        while reader.get(right) < target:
            left = right
            right <<= 1

        while left <= right:
            mid = (left + right) >> 1
            num = reader.get(mid)

            if num == target:
                return mid
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


class Solution:
    def search(self, reader: "ArrayReader", target: int) -> int:
        if reader.get(0) == target:
            return 0

        left, right = 0, 1

        while reader.get(right) < target:
            left = right
            right <<= 1

        while left <= right:
            mid = (left + right) // 2
            num = reader.get(mid)

            if num == target:
                return mid

            if num < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


class Solution:
    def search(self, reader: "ArrayReader", target: int) -> int:
        left, right = 0, 1

        while reader.get(right) < target:
            left = right
            right <<= 1

        while left <= right:
            mid = (left + right) >> 1
            num = reader.get(mid)

            if num == target:
                return mid
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


##
##############################
class Solution:
    def search(self, reader: "ArrayReader", target: int) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().search([-1, 0, 3, 5, 9, 12], 9), 4)
        self.assertEqual(Solution().search([-1, 0, 3, 5, 9, 12], 2), -1)


if __name__ == "__main__":
    unittest.main()
