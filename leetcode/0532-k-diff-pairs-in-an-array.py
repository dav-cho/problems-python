##
#### K-diff Pairs in an Array (medium)
########################################

# Given an array of integers nums and an integer k, return the number of unique
# k-diff pairs in the array.

# A k-diff pair is an integer pair (nums[i], nums[j]), where the following are
# true:

# 0 <= i, j < nums.length
# i != j
# nums[i] - nums[j] == k
# Notice that |val| denotes the absolute value of val.

# Example 1:
# Input: nums = [3,1,4,1,5], k = 2
# Output: 2
# Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
# Although we have two 1s in the input, we should only return the number of unique pairs.

# Example 2:
# Input: nums = [1,2,3,4,5], k = 1
# Output: 4
# Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

# Example 3:
# Input: nums = [1,3,1,5,4], k = 0
# Output: 1
# Explanation: There is one 0-diff pair in the array, (1, 1).

################################################################################

from collections import Counter


## hash map
##############################
class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        counts = Counter(nums)
        res = 0
        for num in counts:
            if k > 0 and num + k in counts:
                res += 1
            elif k == 0 and counts[num] > 1:
                res += 1
                
        return res


## two-pointers
##############################
class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, 1
        res = 0
        while left < n and right < n:
            diff = nums[right] - nums[left]
            if left == right or diff < k:
                right += 1
            elif diff > k:
                left += 1
            else:
                left += 1
                res += 1
                while left < n and nums[left] == nums[left - 1]:
                    left += 1
                    
        return res


## brute force (TLE)
##############################
class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        s_nums = sorted(nums)
        n = len(s_nums)
        res = 0
        for i in range(n):
            if (i > 0 and s_nums[i] == s_nums[i - 1]):
                continue
            for j in range(i + 1, n):
                if (j > i + 1 and s_nums[j] == s_nums[j - 1]):
                    continue
                    
                if abs(s_nums[j] - s_nums[i] == k):
                    res += 1
                    
        return res


## 
##############################
class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().findPairs([3,1,4,1,5], 2), 2)
        self.assertEqual(Solution().findPairs([1,2,3,4,5], 1), 4)
        self.assertEqual(Solution().findPairs([1,3,1,5,4], 0), 1)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Brute Force
##############################
# Time: O(N^2) - Where N is the size of nums.
# - The time complexity for sorting is O(NlogN) while the time complexity for
#   going through ever pair in the nums is O(N^2). Therefore, the final time
#   complexity is O(NlogN)+O(N^2)≈O(N^2).

# Space: O(N) - Where N is the size of nums.
# - This space complexity is incurred by the sorting algorithm. Space
#   complexity is bound to change depending on the sorting algorithm you use.
#   There is no additional space required for the part with two for loops,
#   apart from a single variable result. Therefore, the final space complexity
#   is O(N)+O(1)≈O(N).

# Addendum: We can also approach this problem using brute force without sorting
#           nums. First, we have to create a hash set which will record pairs
#           of numbers whose difference is k. Then, we look for every possible
#           pair. As soon as we find a pair (say i and j) whose difference is
#           k, we add (i, j) and (j, i) to the hash set and increment our
#           placeholder result variable. Whenever we encounter another pair
#           which is already in the hash set, we simply ignore that pair. By
#           doing so we have a better practical runtime (since we are
#           eliminating the sorting step) even though the time complexity is
#           still O(N^2) where N is the size of nums.
class Solution:
    def findPairs(self, nums, k):

        s_nums = sorted(nums)

        result = 0

        for i in range(len(s_nums)):
            if (i > 0 and s_nums[i] == s_nums[i - 1]):
                continue
            for j in range(i + 1, len(s_nums)):
                if (j > i + 1 and s_nums[j] == s_nums[j - 1]):
                    continue

                if abs(s_nums[j] - s_nums[i] == k):
                    result += 1

        return result


## Approach 2: Two Pointers
##############################
# Time: O(NlogN) - Where N is the size of nums.
# - The time complexity for sorting is O(NlogN) while the time complexity for
#   going through nums is O(N). One might mistakenly think that it should be
#   O(N^2) since there is another while loop inside the first while loop. The
#   while loop inside is just incrementing the pointer to skip numbers which
#   are the same as the previous number. The animation should explain this
#   behavior clearer. Therefore, the final time complexity is
#   O(NlogN)+O(N)≈O(NlogN).
# Space: O(N) - Where N is the size of nums.
# - Similar to approach 1, this space complexity is incurred by the sorting
#   algorithm. Space complexity is bound to change depending on the sorting
#   algorithm you use. There is no additional space required for the part where
#   two pointers are being incremented, apart from a single variable result.
#   Therefore, the final space complexity is O(N)+O(1)≈O(N).
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)

        left = 0
        right = 1

        result = 0

        while (left < len(nums) and right < len(nums)):
            if (left == right or nums[right] - nums[left] < k):
                # List item 1 in the text
                right += 1
            elif nums[right] - nums[left] > k:
                # List item 2 in the text
                left += 1
            else:
                # List item 3 in the text
                left += 1
                result += 1
                while (left < len(nums) and nums[left] == nums[left - 1]):
                    left += 1

        return result


## Approach 3: Hashmap
##############################
# Time: O(N)
# - It takes O(N) to create an initial frequency hash map and another O(N) to
#   traverse the keys of that hash map. One thing to note about is the hash key
#   lookup. The time complexity for hash key lookup is O(1) but if there are
#   hash key collisions, the time complexity will become O(N). However those
#   cases are rare and thus, the amortized time complexity is O(2N)≈O(N).
# Space: O(N)
# - We keep a table to count the frequency of each unique number in the input.
#   In the worst case, all numbers are unique in the array. As a result, the
#   maximum size of our table would be O(N).

from collections import Counter

class Solution:
    def findPairs(self, nums, k):
        result = 0

        counter = Counter(nums)

        for x in counter:
            if k > 0 and x + k in counter:
                result += 1
            elif k == 0 and counter[x] > 1:
                result += 1
        return result


