##
#### Sherlock and Anagrams (medium)
#######################################


def sherlockAndAnagrams(s: str) -> int:
    pass


def test(*args):
    count = 0

    def run():
        for test in args:
            nonlocal count
            count += 1
            result = sherlockAndAnagrams(test[0], test[1])
            print(f"test: {count}")
            print(f"result {count}: {result}")

    return run


tests = ["abba", "abcd", "ifailuhkqq", "kkkk", "cdcd"]
#          4       0          3          10       5

test(*tests)
