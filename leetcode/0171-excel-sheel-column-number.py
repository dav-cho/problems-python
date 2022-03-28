##
#### 171. Excel Sheet Column Number (easy)
##############################################


# right to left
def titleToNumber(columnTitle: str) -> int:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_map = {alphabet[i]: i + 1 for i in range(26)}
    count = 0

    length = len(columnTitle)
    for i in range(length):
        current = columnTitle[-1 - i]
        count += alpha_map[current] * (26**i)

    return count


# left to right
def titleToNumber(columnTitle: str) -> int:
    count = 0

    for i in range(len(columnTitle)):
        count = count * 26 + (ord(columnTitle[i]) - ord("A") + 1)

    return count


# tests = ["A", "AB", "ZY"]
tests = ["A", "AB", "ZY", "FXSHRXW"]
#         1    28    701  2147483647


def test(arr):
    count = 1

    def run():
        for test in arr:
            result = titleToNumber(test)
            nonlocal count
            print(f"~ test {count}")
            print(f"{test} --> {result}")
            count += 1

    return run()


test(tests)
