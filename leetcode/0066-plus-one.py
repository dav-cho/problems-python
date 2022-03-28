##
#### 66. Plus One (easy)
########################################


## best*
##############################
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits[-1] += 1
        carry = 0

        for i in range(len(digits) - 1, -1, -1):
            carry, digits[i] = divmod(digits[i] + carry, 10)

        return [carry] + digits if carry else digits


## attempt 1
##############################
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits[-1] += 1
        carry = 0

        for i in range(len(digits) - 1, -1, -1):
            carry, new_digit = divmod(digits[i] + carry, 10)
            digits[i] = new_digit

        return [carry] + digits if carry else digits


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits[-1] += 1
        remainder = 0

        for i in range(len(digits) - 1, -1, -1):
            new_digit = digits[i] + remainder
            remainder, new_digit = divmod(new_digit, 10)
            digits[i] = new_digit

        if remainder:
            digits.insert(0, remainder)

        return digits


##
##############################
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits[-1] += 1
        carry = 0

        for i in range(len(digits) - 1, -1, -1):
            carry, digit = divmod(digits[i] + carry, 10)
            digits[i] = digit

        return [carry] + digits if carry else digits


## recursive
##############################
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if len(digits) == 0:
            return [1]

        if digits[-1] != 9:
            return digits[:-1] + [digits[-1] + 1]

        return self.plusOne(digits[:-1]) + [0]


## recursive (not working)
##############################
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if len(digits) == 0:
            digits = [1]
        elif digits[-1] == 9:
            digits = self.plusOne(digits[:-1])
        else:
            digits[-1] += 1

        return digits


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.plusOne([1, 2, 3]), [1, 2, 4])
        self.assertEqual(solution.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])
        self.assertEqual(solution.plusOne([0]), [1])


if __name__ == "__main__":
    unittest.main()
