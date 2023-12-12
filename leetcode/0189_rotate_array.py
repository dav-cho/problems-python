##
#### 189. Rotate Array (medium)
###################################


## cyclic replacements
##############################
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        start_idx, count = 0, n
        while count:
            prev = nums[start_idx]
            curr_idx = start_idx
            while True:
                next_idx = (curr_idx + k) % n
                prev, nums[next_idx] = nums[next_idx], prev
                curr_idx = next_idx
                count -= 1
                if curr_idx == start_idx:
                    break

            start_idx += 1


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        N = len(nums)
        k %= N
        start = 0
        count = N

        while count:
            prev = nums[start]
            curr = start

            while True:
                next_idx = (curr + k) % N
                prev, nums[next_idx] = nums[next_idx], prev
                curr = next_idx
                count -= 1

                if curr == start:
                    break

            start += 1


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            prev = nums[start]
            curr = start

            while True:
                next_idx = (curr + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                curr = next_idx
                count += 1

                if curr == start:
                    break
            start += 1


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            curr, prev = start, nums[start]

            while True:
                next_idx = (curr + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                curr = next_idx
                count += 1

                if curr == start:
                    break
            start += 1


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        N = len(nums)
        k %= N
        start = count = 0

        while count < N:
            prev = nums[start]
            curr = start

            while True:
                next_idx = (curr + k) % N

                temp = prev
                prev = nums[next_idx]
                nums[next_idx] = temp
                curr = next_idx
                count += 1

                if curr == start:
                    break

            start += 1


## extra array
##############################
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        N = len(nums)
        temp = [None] * N

        for i in range(N):
            temp[(i + k) % N] = nums[i]

        nums[:] = temp


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]

        nums[:] = a


## reverse
##############################
class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)


## brute force(TLE)
##############################
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k %= len(nums)

        for i in range(k):
            prev = nums[-1]
            for j in range(len(nums)):
                nums[j], prev = prev, nums[j]


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(
            solution.rotate([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4]
        )
        self.assertEqual(solution.rotate([-1, -100, 3, 99], 2), [3, 99, -1, -100])


if __name__ == "__main__":
    unittest.main()
