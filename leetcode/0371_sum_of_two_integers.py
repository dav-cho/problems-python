##
#### 371. Sum of Two Integers (medium)
##########################################


class Solution:
    def getSum(self, a: int, b: int) -> int:
        pass


## Tests
############
def test(*args):
    solution = Solution()
    count = 0

    def run():
        for test in args:
            nonlocal count
            count += 1
            result = solution.getSum(test[0], test[1])
            print(f"test {count}")
            print(f"result {count}: {result}")

    return run()


test1 = (1, 2)  # 3
test2 = (2, 3)  # 5

test(test1, test2)
