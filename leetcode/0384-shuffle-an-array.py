##
#### Shuffle an Array (medium)
########################################

# Given an integer array nums, design an algorithm to randomly shuffle the
# array. All permutations of the array should be equally likely as a result of
# the shuffling.

# Implement the Solution class:
# - Solution(int[] nums) Initializes the object with the integer array nums.
# - int[] reset() Resets the array to its original configuration and returns it.
# - int[] shuffle() Returns a random shuffling of the array.

# Example 1:
# Input
# ["Solution", "shuffle", "reset", "shuffle"]
# [[[1, 2, 3]], [], [], []]
# Output
# [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
# Explanation
# Solution solution = new Solution([1, 2, 3]);
# solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
#                        // Any permutation of [1,2,3] must be equally likely to be returned.
#                        // Example: return [3, 1, 2]
# solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
# solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

# Constraints:
# 1 <= nums.length <= 200
# -106 <= nums[i] <= 106
# All the elements of nums are unique.
# At most 5 * 104 calls in total will be made to reset and shuffle.

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

################################################################################

## fisher-yates algorithm
##############################
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        self.nums = list(self.original)
        
        return self.nums

    def shuffle(self) -> List[int]:
        N = len(self.nums)
        
        for i in range(N):
            rand_idx = random.randrange(i, N)
            self.nums[i], self.nums[rand_idx] = self.nums[rand_idx], self.nums[i]
            
        return self.nums


## brute force
##############################
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        self.nums = list(self.original)
        
        return self.nums

    def shuffle(self) -> List[int]:
        nums_copy = list(self.nums)
        
        for i in range(len(self.nums)):
            remove_idx = random.randrange(len(nums_copy))
            self.nums[i] = nums_copy.pop(remove_idx)
            
        return self.nums


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Brute Force [Accepted]
#########################################
# Time: O(n^2) - The quadratic time complexity arises from the calls to
#                list.remove (or list.pop), which run in linear time. n linear
#                list removals occur, which results in a fairly easy quadratic
#                analysis.
# Space: O(n) - Because the problem also asks us to implement reset, we must
#               use linear additional space to store the original array.
#               Otherwise, it would be lost upon the first call to shuffle.
class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        aux = list(self.array)

        for idx in range(len(self.array)):
            remove_idx = random.randrange(len(aux))
            self.array[idx] = aux.pop(remove_idx)

        return self.array


## Approach 2: Fisher-Yates Algorithm [Accepted]
####################################################
# Time: O(n) - The Fisher-Yates algorithm runs in linear time, as generating a
#              random index and swapping two values can be done in
#              constant time.
# Space: O(n) - Although we managed to avoid using linear space on the
#               auxiliary array from the brute force approach, we still need it
#               for reset, so we're stuck with linear space complexity.
class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array


## Approach 3: 
##############################
# Time: 
# Space: 


