##
#### Sherlock and Anagrams (medium)
#######################################

# Two strings are anagrams of each other if the letters of one
# string can be rearranged to form the other string.
# Given a string, find the number of pairs of substrings of
# the string that are anagrams of each other.


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
