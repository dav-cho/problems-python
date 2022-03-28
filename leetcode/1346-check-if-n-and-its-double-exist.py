##
#### 1346. Check If N and Its Double Exist (easy)
#####################################################


class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        doubles = [2 * m for m in arr]

        for i, num in enumerate(arr):
            if num in doubles:
                if i != doubles.index(num):
                    return True

        return False


class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        for i, num in enumerate(arr):
            if num * 2 in arr:
                if i != arr.index(num * 2):
                    return True

        return False


## Tests
############

solution = Solution()
print(solution.checkIfExist([10, 2, 5, 3]))
