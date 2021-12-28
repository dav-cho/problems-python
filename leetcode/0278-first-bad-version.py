##
#### First Bad Version (easy)
########################################

# You are a product manager and currently leading a team to develop a new
# product. Unfortunately, the latest version of your product fails the quality
# check. Since each version is developed based on the previous version, all the
# versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first
# bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version
# is bad. Implement a function to find the first bad version. You should
# minimize the number of calls to the API.

# Example 1:
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.

# Example 2:
# Input: n = 1, bad = 1
# Output: 1
 
# Constraints:
# 1 <= bad <= n <= 231 - 1

################################################################################

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


## binary search / divide and conquer
#########################################
class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n
        
        while left < right:
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
                
        return left


class Solution:
    def firstBadVersion(self, n):
        left = 1
        right = n
        
        while left < right:
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
                
        return right


class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n
        
        while left < right:
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
                
        return left


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.firstBadVersion(5), 4)
        self.assertEqual(solution.firstBadVersion(1), 1)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: (Linear Scan) [Time Limit Exceeded]
######################################################
# Time: O(n) - Assume that isBadVersion(version) takes constant time to check
#              if a version is bad. It takes at most n - 1 checks, therefore
#              the overall time complexity is O(n).
# Space: O(1)

## Java
#public int firstBadVersion(int n) {
#    for (int i = 1; i < n; i++) {
#        if (isBadVersion(i)) {
#            return i;
#        }
#    }
#    return n;
#}


## Approach 2: (Binary Search) [Accepted]
#############################################
# Time: O(logn) - The search space is halved each time, so the time complexity
#                 is O(logn).
# Space: O(1)

## Java
#public int firstBadVersion(int n) {
#    int left = 1;
#    int right = n;
#    while (left < right) {
#        int mid = left + (right - left) / 2;
#        if (isBadVersion(mid)) {
#            right = mid;
#        } else {
#            left = mid + 1;
#        }
#    }
#    return left;
#}


