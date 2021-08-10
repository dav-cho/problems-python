##
#### Daily Temperatures (medium)
####################################

# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to
# wait after the ith day to get a warmer temperature. If there is no future day
# for which this is possible, keep answer[i] == 0 instead.

# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]

# Constraints:
# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

################################################################################

## 
######################
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_idx = stack.pop()
                answer[prev_idx] = i - prev_idx
            stack.append(i)

        return answer


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        length = len(temperatures)
        right_max = float('-inf')
        answer = [0] * length

        for i in range(length - 1, -1, -1):
            temp = temperatures[i]
            if right_max <= temp:
                right_max = temp
            else:
                days = 1
                while temperatures[i + days] <= temp:
                    days += answer[i + days]
                answer[i] = days

        return answer


## Tests
#############

test1 = [73,74,75,71,69,72,76,73]           # [1,1,4,2,1,1,0,0]
test2 = [30,40,50,60]                       # [1,1,1,0]
test3 = [30,60,90]                          # [1,1,0]
test4 = [89,62,70,58,47,47,46,76,100,70]    # [8,1,5,4,3,2,1,1,0,0]

tests = [
    test1,
    test2,
    test3,
    test4
]


def test(*args):
    count = 1

    def run():
        for test in args:
            nonlocal count
            print(f"~ test{count}")
            count += 1 

            solution = Solution()
            result = solution.dailyTemperatures(test)

            print(result)

    return run()


test(*tests)


## LeetCode Solutions
#########################

## Approach 1: 
###################
# Time: 
# Space: 


## Approach 2: 
###################
# Time: 
# Space: 


## Approach 3: 
###################
# Time: 
# Space: 


