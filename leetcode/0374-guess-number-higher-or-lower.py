##
#### Guess Number Higher or Lower (easy)
############################################

# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked is
# higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns 3 possible
# results:

#   -1: The number I picked is lower than your guess (i.e. pick < num).
#    1: The number I picked is higher than your guess (i.e. pick > num).
#    0: The number I picked is equal to your guess (i.e. pick == num).

# Return the number that I picked.

# Example 1:
# Input: n = 10, pick = 6
# Output: 6

# Example 2:
# Input: n = 1, pick = 1
# Output: 1

# Example 3:
# Input: n = 2, pick = 1
# Output: 1
 
# Constraints:
# 1 <= n <= 231 - 1
# 1 <= pick <= n

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

################################################################################


## binary search
##############################
class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        
        while left <= right:
            mid = left + (right - left) // 2
            res = guess(mid)
            
            if res == 0:
                return mid
            elif res > 0:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1


## ternary search
##############################
class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        
        while left <= right:
            mid1 = left + (right - left) // 3
            mid2 = right - (right - left) // 3
            res1 = guess(mid1)
            res2 = guess(mid2)
            
            if res1 == 0:
                return mid1
            if res2 == 0:
                return mid2
            elif res1 < 0:
                right = mid1 - 1
            elif res2 > 0:
                left = mid2 + 1
            else:
                left = mid1 + 1
                right = mid2 - 1
            
        return -1


## brute force
##############################
class Solution:
    def guessNumber(self, n: int) -> int:
        for num in range(1, n):
            if guess(num) == 0:
                return num
            
        return n


## first attempt
##############################
class Solution:
    LOWER = -1
    HIGHER = 1
    EQUALS = 0
    
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        
        while left <= right:
            num = (left + right) // 2
            curr_guess = guess(num)
            
            if curr_guess == Solution.EQUALS:
                return num
            elif curr_guess == Solution.HIGHER:
                left = num + 1
            else:
                right = num - 1
                
        return right


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().guessNumber(10), 6)
        self.assertEqual(Solution().guessNumber(1), 1)
        self.assertEqual(Solution().guessNumber(2), 1)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Brute Force
##############################
# Time: O(n) - We scan all the numbers from 1 to n.
# Space: O(1) - No extra space is used.

## Java
#public class Solution extends GuessGame {
#    public int guessNumber(int n) {
#        for (int i = 1; i < n; i++)
#            if (guess(i) == 0)
#                return i;
#        return n;
#    }
#}


## Approach 2: Using Binary Search
######################################
# Time: O(log_2(n)) - Binary Search is used.
# Space: O(1) - No extra space is used.

## Java
#public class Solution extends GuessGame {
#    public int guessNumber(int n) {
#        int low = 1;
#        int high = n;
#        while (low <= high) {
#            int mid = low + (high - low) / 2;
#            int res = guess(mid);
#            if (res == 0)
#                return mid;
#            else if (res < 0)
#                high = mid - 1;
#            else
#                low = mid + 1;
#        }
#        return -1;
#    }
#}


## Approach 3: 
##############################
# Time: O(log_3(n)) - Ternary Search is used.
# Space: O(1) - No extra space is used.

## Java
#public class Solution extends GuessGame {
#    public int guessNumber(int n) {
#        int low = 1;
#        int high = n;
#        while (low <= high) {
#            int mid1 = low + (high - low) / 3;
#            int mid2 = high - (high - low) / 3;
#            int res1 = guess(mid1);
#            int res2 = guess(mid2);
#            if (res1 == 0)
#                return mid1;
#            if (res2 == 0)
#                return mid2;
#            else if (res1 < 0)
#                high = mid1 - 1;
#            else if (res2 > 0)
#                low = mid2 + 1;
#            else {
#                low = mid1 + 1;
#                high = mid2 - 1;
#            }
#        }
#        return -1;
#    }
#}


## Follow up:
##############################
# It seems that ternary search is able to terminate earlier compared to binary
# search. But why is binary search more widely used?

## Comparisons between Binary Search and Ternary Search

# Ternary Search is worse than Binary Search. The following outlines the
# recursive formula to count comparisons of Binary Search in the worst case.

#       T(n) = T(n/2) + 2, T(1) = 1
#       T(n/2) = T(n/(2**2)) + 2

#    ∴  T(n) = T(n/(2**2)) + 2 * 2
#            = T(n/(2**3)) + 3 * 2
#            = ...
#            = T(n/(2**(log_2(n)))) + 2log_2(n)
#            = T(1) + 2log_2(n)
#            = 1 + 2log_2(n)

# The following outlines the recursive formula to count comparisons of Ternary
# Search in the worst case.

#       T(n) = T(n/3) + 4, T(1) = 1
#       T(n/3) = T(n/(3**2)) + 4

#    ∴  T(n) = T(n/(3**2)) + 2 * 4
#            = T(n/(3**3)) + 3 * 4
#            = ...
#            = T(n/(3**(log_3(n)))) + 4log_3(n)
#            = T(1) + 4log_3(n)
#            = 1 + 4log_3(n)

# As shown above, the total comparisons in the worst case for ternary and
# binary search are 1 + 4 log_3(n) and 1 + 2log_2(n) comparisons respectively.
# To determine which is larger, we can just look at the expression 2log_3(n)
# and log_2(n). The expression 2log_3(n) can be written as
# 2/(log_2(3)) * log_2(n). Since the value of 2/(log_2(3)) is greater than one,
# Ternary Search does more comparisons than Binary Search in the worst case.


