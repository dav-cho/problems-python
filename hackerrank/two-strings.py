##
#### Two Strings (easy)
############################


def twoStrings(s1: str, s2: str) -> str:
    # a = s1 if len(s1) < len(s2) else s2
    # b = s2 if a is s1 else s1

    # for char in a:
    #     if char in b:
    #         return "YES"

    for char in s1:
        if char in s2:
            return "YES"

    return "NO"


def test(*args):
    count = 0

    def run():
        for test in args:
            nonlocal count
            count += 1
            result = twoStrings(test[0], test[1])
            print(f"test: {count}")
            print(f"result {count}: {result}")

    return run


test1 = ["hello", "world"]  # 'YES'
test2 = ["hi", "world"]  # 'NO'
test3 = ["and", "art"]  # 'YES'
test4 = ["be", "cat"]  # 'NO'

test(test1, test2, test3, test4)()
