##
#### Climbing Stairs (easy)
###############################

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?


# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Constraints:
# 1 <= n <= 45

###########################################################################

## Approach 1: Brute Force
##############################
class Solution:
    def climbStairs(n: int) -> int:
        pass


## Approach 2: Recursion with Memoization
#############################################
class Solution:
    def climbStairs(n: int) -> int:
        pass


## Approach 3: Dynamic Programming
######################################
class Solution:
    def climbStairs(n: int) -> int:
        pass


## Approach 4: Fibonacci Number
###################################
class Solution:
    def climbStairs(n: int) -> int:
        pass


def test(tests_arr):
    test_number = 0

    def run_test():
        for test in tests_arr:
            nonlocal test_number
            test_number += 1
            result = climbStairs(test)
            print(f"~ test {test_number}")
            print(f"    case:   {test}")
            print(f"    result: {result}")

    return run_test


tests = [2, 3]
#        2  3

test(tests)()


## LeetCode Solutions
#########################


## Approach 1: Brute Force
##############################
# time: O(2^N)
# space: O(N)
def climbStairs(n: int) -> int:
    def climb(i, n):
        if i > n:
            return 0
        if i is n:
            return 1

        return climb(i + 1, n) + climb(i + 2, n)

    return climb(0, n)


## Java
# public class Solution {
#     public int climbStairs(int n) {
#         int memo[] = new int[n + 1];
#         return climb_Stairs(0, n, memo);
#     }
#     public int climb_Stairs(int i, int n, int memo[]) {
#         if (i > n) {
#             return 0;
#         }
#         if (i == n) {
#             return 1;
#         }
#         if (memo[i] > 0) {
#             return memo[i];
#         }
#         memo[i] = climb_Stairs(i + 1, n, memo) + climb_Stairs(i + 2, n, memo);
#         return memo[i];
#     }
# }


## Approach 2: Recursion with Memoization
#############################################
# time: O(n) - size of recursion tree can go up to n
# space: O(n) - depth of recursion tree can go up to n
def climbStairs(n: int) -> int:
    climbed = {}

    def climb(i, n):
        if i > n:
            return 0
        if i is n:
            return 1
        # if i in climbed and climbed[i] > 0:
        if i in climbed:
            return climbed[i]

        climbed[i] = climb(i + 1, n) + climb(i + 2, n)

        return climbed[i]

    return climb(0, n)


## Java
# public class Solution {
#     public int climbStairs(int n) {
#         int memo[] = new int[n + 1];
#         return climb_Stairs(0, n, memo);
#     }
#     public int climb_Stairs(int i, int n, int memo[]) {
#         if (i > n) {
#             return 0;
#         }
#         if (i == n) {
#             return 1;
#         }
#         if (memo[i] > 0) {
#             return memo[i];
#         }
#         memo[i] = climb_Stairs(i + 1, n, memo) + climb_Stairs(i + 2, n, memo);
#         return memo[i];
#     }
# }

## Approach 3: Dynamic Programming
######################################
# time: O(n) - single loop up to n
# space: O(n) - dp array of size n is used
# one can reach step i in one of two ways:
#       take a single step from (i - 1)
#       take two steps from (i - 2)
# so the total number of ways to reach step i is equal to the sum of
# ways of reaching (i - 1) step and ways of reaching (i -2) step.
# dp = number of ways to reach step i:
# dp[i] = dp[i - 1] + dp[i - 2]
def climbStairs(n: int) -> int:
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


## Java
# public class Solution {
#     public int climbStairs(int n) {
#         if (n == 1) {
#             return 1;
#         }
#         int[] dp = new int[n + 1];
#         dp[1] = 1;
#         dp[2] = 2;
#         for (int i = 3; i <= n; i++) {
#             dp[i] = dp[i - 1] + dp[i - 2];
#         }
#         return dp[n];
#     }
# }

## Approach 4: Fibonacci Number
###################################
# time: O(n) - Single loop up to n is required to calculate nth fibonacci number
# space: O(1) - Constant space is used
class Solution:
    def climbStairs(n: int) -> int:
        pass


## Java
# public class Solution {
#     public int climbStairs(int n) {
#         if (n == 1) {
#             return 1;
#         }
#         int first = 1;
#         int second = 2;
#         for (int i = 3; i <= n; i++) {
#             int third = first + second;
#             first = second;
#             second = third;
#         }
#         return second;
#     }
# }
