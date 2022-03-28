##
#### 739. Daily Temperatures (medium)
#########################################


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
        right_max = float("-inf")
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

test1 = [73, 74, 75, 71, 69, 72, 76, 73]  # [1,1,4,2,1,1,0,0]
test2 = [30, 40, 50, 60]  # [1,1,1,0]
test3 = [30, 60, 90]  # [1,1,0]
test4 = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]  # [8,1,5,4,3,2,1,1,0,0]

tests = [test1, test2, test3, test4]


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
