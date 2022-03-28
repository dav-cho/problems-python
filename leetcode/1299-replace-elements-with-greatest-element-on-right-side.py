##
#### 1299. Replace Elements with Greatest Element on Right Side (easy)
##########################################################################


class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        for i in range(len(arr) - 1):
            max = i + 1

            for j in range(i + 1, len(arr)):
                if arr[j] > arr[max]:
                    max = j

            arr[i] = arr[max]

        arr[-1] = -1

        return arr


class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        mx = -1

        for i in range(len(arr) - 1, -1, -1):
            arr[i], mx = mx, max(mx, arr[i])

        return arr


## Tests
############

test1 = [17, 18, 5, 4, 6, 1]  # [18, 6, 6, 6, 1, -1]
test2 = [400]  # [-1]
test3 = [57010, 40840, 69871, 14425, 70605]  # [70605, 70605, 70605, 70605, -1]


def test(*args):
    solution = Solution()
    count = 1

    def run():
        for test in args:
            nonlocal count
            print("~ test", count)
            print(test)

            result = solution.replaceElements(test)
            count += 1

            print(result)

    return run()


test(test1, test2, test3)
