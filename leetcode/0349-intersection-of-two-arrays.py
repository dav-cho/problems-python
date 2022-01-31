##
#### Intersection of Two Arrays (easy)
#########################################

# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must be unique and you may return
# the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
 
# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

################################################################################


## binary search
##############################
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)
        
        nums2.sort()
        res = set()
        
        for num in nums1:
            if self.search(nums2, num):
                res.add(num)
                
        return list(res)
        
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) >> 1
            
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False


## two sets
##############################
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        return [x for x in set1 if x in set2]


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        if len(set1) > len(set2):
            return self.intersection(nums2, nums1)
        
        return [x for x in set1 if x in set2]


## built in intersection
##############################
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        return list(set1 & set2)


## first attempt
##############################
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        res = []

        for num in set1:
            if num in set2:
                res.append(num)
                
        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertCountEqual(Solution().intersection([1,2,2,1], [2,2]), [2])
        self.assertCountEqual(Solution().intersection([4,9,5], [9,4,9,8,4]), [9,4])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Two Sets
##############################
# Time: O(n + m) - Where n and m are arrays' lengths. O(n) time is used to
#                  convert nums1 into set, O(m) time is used to convert nums2,
#                  and contains/in operations are O(1) in the average case.
# Space: O(m + n) - In the worst case when all elements in the arrays are
#                   different.
class Solution:
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]
        
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """  
        set1 = set(nums1)
        set2 = set(nums2)
        
        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)


## Approach 2: Built-in Set Intersection
############################################
# Time: O(n + m) - In the average case and O(n × m) in the worst case when
#                  load factor is high enough.
# Space: O(n+m) in the worst case when all elements in the arrays are different.
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """  
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)


