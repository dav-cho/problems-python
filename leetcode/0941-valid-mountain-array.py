##
#### 941. Valid Mountain Array (easy)
#########################################


class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        i, last = 0, len(arr) - 1

        while i < last and arr[i] < arr[i + 1]:
            i += 1

        if i == 0 or i == last:
            return False

        while i < last and arr[i] > arr[i + 1]:
            i += 1

        return i == last


## Tests
############

test1 = [2, 1]  # False
test2 = [3, 5, 5]  # False
test3 = [0, 3, 2, 1]  # True

tests = [test1, test2, test3]


def test(*args):
    solution = Solution()
    count = 1

    def run():
        for test in args:
            nonlocal count
            print("~ test", count)
            print(test)

            result = solution.validMountainArray(test)

            print(result)

    return run()


test(*tests)
