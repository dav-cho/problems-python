##
#### Contains Duplicate (easy)
##################################

# Given an integer array nums, return true if any value appears at least
# twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

#############################################################################

## sorting
##############################
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
            
        return False


## hash set
##############################
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.containsDuplicate([1,2,3,1]), True)
        self.assertEqual(solution.containsDuplicate([1,2,3,4]), False)
        self.assertEqual(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]), True)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: (Naive Linear Search) [Time Limit Exceeded]
##############################################################
# Time: O(n^2) - In the worst case, there are (n(n = 1))/2 pairs of integeres to
#                check. Therefore, the time complexity is O(n^2).
# Space: O(1) - We only used constant extra space.

# This approach will get Time Limit Exceeded on LeetCode. Usually, if an
# algorithm is O(n^2), it can handle nn up to around 10^4. It gets Time Limit
# Exceeded when n n≥10^5.

## Java
#public boolean containsDuplicate(int[] nums) {
#    for (int i = 0; i < nums.length; ++i) {
#        for (int j = 0; j < i; ++j) {
#            if (nums[j] == nums[i]) return true;  
#        }
#    }
#    return false;
#}
#// Time Limit Exceeded


## Approach 2: (Sorting) [Accepted]
#######################################
# Time: O(n log(n)) - Sorting is O(n log(n)) and the sweeping is O(n). The
#                     entire algorithm is dominated by the sorting step, which
#                     is O(n log(n)).
# Space: O(1) - Space depends on the sorting implementation which, usually,
#               costs O(1) auxilary space if heapsort is used.

## Java
#public boolean containsDuplicate(int[] nums) {
#    Arrays.sort(nums);
#    for (int i = 0; i < nums.length - 1; ++i) {
#        if (nums[i] == nums[i + 1]) return true;
#    }
#    return false;
#}

# *Note:
# The implementation here modifies the original array by sorting it. In general,
# it is not a good practice to modify the input unless it is clear to the caller
# that the input will be modified. One may make a copy of nums and operate on
# the copy instead.


## Approach 3: (Hash Table) [Accepted]
##########################################
# Time: O(n) - We do search() and insert() for n times and each operation takes
#              constant time.
# Space: O(n) - The space used by a hash table is linear with the number of
#               elements in it.

## Java
#public boolean containsDuplicate(int[] nums) {
#    Set<Integer> set = new HashSet<>(nums.length);
#    for (int x: nums) {
#        if (set.contains(x)) return true;
#        set.add(x);
#    }
#    return false;
#}

# *Note:
# For certain test cases with not very large n, the runtime of this method can
# be slower than Approach #2. The reason is hash table has some overhead in
# maintaining its property. One should keep in mind that real world performance
# can be different from what the Big-O notation says. The Big-O notation only
# tells us that for sufficiently large input, one will be faster than the other.
# Therefore, when n is not sufficiently large, an O(n) algorithm can be slower
# than an O(nlogn) algorithm.

