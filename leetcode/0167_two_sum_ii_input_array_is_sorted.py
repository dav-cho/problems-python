##
#### 167. Two Sum II - Input array is sorted (easy)
#######################################################


## best - two pointer
##############################
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                return [left + 1, right + 1]


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            if curr_sum > target:
                right -= 1
            if curr_sum < target:
                left += 1


## two pointer
##############################
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            if curr_sum > target:
                right -= 1
            if curr_sum < target:
                left += 1


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            elif curr_sum > target:
                right -= 1
            else:
                left += 1


## one-pass hash
##############################
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(numbers):
            comp = target - num
            if comp in seen:
                return [seen[comp], i + 1]

            seen[num] = i + 1


## two-pass hash
##############################
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(numbers):
            seen[num] = i
        for i, num in enumerate(numbers):
            comp = target - num
            if comp in seen:
                return [i + 1, seen[comp] + 1]


## brute force
##############################
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]


## first attempt - one pass hash
####################################
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(numbers):
            comp = target - num
            if comp in seen:
                return [seen[comp], i + 1]

            seen[num] = i + 1


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.twoSum([2, 7, 11, 15], 9), [1, 2])
        self.assertEqual(solution.twoSum([2, 3, 4], 6), [1, 3])
        self.assertEqual(solution.twoSum([-1, 0], -1), [1, 2])


if __name__ == "__main__":
    unittest.main()
