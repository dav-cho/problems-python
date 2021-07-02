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


# Approach 1: Brute Force
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


# Approach 2: Recursion with Memoization
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


# Approach 3: Dynamic Programming
# one can reach step i in one of two ways:
#       take a single step from (i - 1)
#       take two steps from (i - 2)
# so the total number of ways to reach step i is equal to the sum of
# ways of reaching (i - 1) step and ways of reaching (i -2) step.
# dp = number of ways to reach step i:
# dp[i] = dp[i - 1] + dp[i - 2]
# time:
# space:
def climbStairs(n: int) -> int:
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


result1 = climbStairs(2)  # 2
result2 = climbStairs(3)  # 3
print("~ result1", result1)
print("~ result2", result2)
