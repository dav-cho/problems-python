##
#### Minimum Difficulty of a Job Schedule (hard)
####################################################

# You want to schedule a list of jobs in d days. Jobs are dependent (i.e To
# work on the ith job, you have to finish all the jobs j where 0 <= j < i).

# You have to finish at least one task every day. The difficulty of a job
# schedule is the sum of difficulties of each day of the d days. The difficulty
# of a day is the maximum difficulty of a job done on that day.

# You are given an integer array jobDifficulty and an integer d. The difficulty
# of the ith job is jobDifficulty[i].

# Return the minimum difficulty of a job schedule. If you cannot find a
# schedule for the jobs return -1.

# Example 1:
# Input: jobDifficulty = [6,5,4,3,2,1], d = 2
# Output: 7
# Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
# Second day you can finish the last job, total difficulty = 1.
# The difficulty of the schedule = 6 + 1 = 7 

# Example 2:
# Input: jobDifficulty = [9,9,9], d = 4
# Output: -1
# Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.

# Example 3:
# Input: jobDifficulty = [1,1,1], d = 3
# Output: 3
# Explanation: The schedule is one job per day. total difficulty will be 3.
 
# Constraints:
# 1 <= jobDifficulty.length <= 300
# 0 <= jobDifficulty[i] <= 1000
# 1 <= d <= 10

################################################################################

from functools import lru_cache


## bottom-up space optimized (1D)
#####################################
class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        dp = [float('inf')] * n
        dp[-1] = jobDifficulty[-1]
        
        for i in range(n - 2, -1, -1):
            dp[i] = max(dp[i + 1], jobDifficulty[i])
            
        for day in range(d - 1, 0, -1):
            for i in range(day - 1, n - (d - day)):
                dp[i] = float('inf')
                hardest = 0
                for j in range(i, n - (d - day)):
                    hardest = max(hardest, jobDifficulty[j])
                    dp[i] = min(dp[i], hardest + dp[j + 1])
                    
        return dp[0]


## bottom-up (2D)
##############################
class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        dp = [[float('inf')] * (d + 1) for _ in range(n)]
        dp[-1][d] = jobDifficulty[-1]
        
        for i in range(n - 2, -1, -1):
            dp[i][d] = max(dp[i + 1][d], jobDifficulty[i])
            
        for day in range(d - 1, 0, -1):
            for i in range(day - 1, n - (d - day)):
                hardest = 0
                for j in range(i, n - (d - day)):
                    hardest = max(hardest, jobDifficulty[j])
                    dp[i][day] = min(dp[i][day], hardest + dp[j + 1][day + 1])
                    
        return dp[0][1]


## top-down
##############################
class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        
        hardest_remaining = [0] * n
        hardest = 0
        for i in range(n - 1, -1, -1):
            hardest = max(hardest, jobDifficulty[i])
            hardest_remaining[i] = hardest
            
        @lru_cache(None)
        def dp(i, day):
            if day == d:
                return hardest_remaining[i]
            
            res = float('inf')
            hardest = 0
            days_remaining = d - day
            for j in range(i, n - days_remaining):
                hardest = max(hardest, jobDifficulty[j])
                res = min(res, hardest + dp(j + 1, day + 1))
                
            return res
        
        return dp(0, 1)


## 
##############################
class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().minDifficulty([6,5,4,3,2,1], 2), 7)
        self.assertEqual(Solution().minDifficulty([9,9,9], 4), -1)
        self.assertEqual(Solution().minDifficulty([1,1,1], 3), 3)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Top-Down from Explore Cards
##############################################
# Time: 
# Space: 
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        # If we cannot schedule at least one job per day, 
        # it is impossible to create a schedule
        if n < d:
            return -1
        
        hardest_job_remaining = [0] * n
        hardest_job = 0
        for i in range(n - 1, -1, -1):
            hardest_job = max(hardest_job, jobDifficulty[i])
            hardest_job_remaining[i] = hardest_job
        
        @lru_cache(None)
        def dp(i, day):
            # Base case, it's the last day so we need to finish all the jobs
            if day == d:
                return hardest_job_remaining[i]
            
            best = float("inf")
            hardest = 0
            # Iterate through the options and choose the best
            for j in range(i, n - (d - day)): # Leave at least 1 job per remaining day
                hardest = max(hardest, jobDifficulty[j])
                best = min(best, hardest + dp(j + 1, day + 1)) # Recurrence relation

            return best
        
        return dp(0, 1)


## Approach 2: Bottom-Up from Explore Cards
###############################################
# Time: 
# Space: 
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        # If we cannot schedule at least one job per day, 
        # it is impossible to create a schedule
        if n < d:
            return -1
        
        dp = [[float("inf")] * (d + 1) for _ in range(n)]
        
        # Set base cases
        dp[-1][d] = jobDifficulty[-1]

        # On the last day, we must schedule all remaining jobs, so dp[i][d]
        # is the maximum difficulty job remaining
        for i in range(n - 2, -1, -1):
            dp[i][d] = max(dp[i + 1][d], jobDifficulty[i])

        for day in range(d - 1, 0, -1):
            for i in range(day - 1, n - (d - day)):
                hardest = 0
                # Iterate through the options and choose the best
                for j in range(i, n - (d - day)):
                    hardest = max(hardest, jobDifficulty[j])
                    # Recurrence relation
                    dp[i][day] = min(dp[i][day], hardest + dp[j + 1][day + 1])

        return dp[0][1]


## Approach 3: 
##############################
# Time: 
# Space: 


