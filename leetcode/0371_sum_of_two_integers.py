##
#### Sum of Two Integers (medium)
#####################################

# Given two integers a and b, return the sum of the two
# integers without using the operators + and -.


# Example 1:
# Input: a = 1, b = 2
# Output: 3

# Example 2:
# Input: a = 2, b = 3
# Output: 5

# Constraints:
# -1000 <= a, b <= 1000

#######################################################################


def getSum(a: int, b: int) -> int:
    pass


test1 = (1, 2)  # 3
test2 = (2, 3)  # 5


def test(*args):
    count = 0

    def run():
        for test in args:
            nonlocal count
            count += 1
            result = getSum(test[0], test[1])
            print(f"test {count}")
            print(f"result {count}: {result}")

    return run()


test(test1, test2)
