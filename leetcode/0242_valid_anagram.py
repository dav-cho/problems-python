##
#### Valid Anagram (easy)
#############################

# Given two strings s and t, return true if t is
# an anagram of s, and false otherwise.


# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# Follow up: What if the inputs contain Unicode characters?
# How would you adapt your solution to such a case?

####################################################################


from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


# Approach 1: Sorting
# time: O(log(n)) - sorting costs O(n log(n)) and comparing costs O(n)
# space: O(1) - language dependent --> space depends on sorting implementation
#               O(1) if heapsort is used
def isAnagram(s: str, t: str) -> bool:
    if len(s) is not len(t):
        return False

    s_sorted, t_sorted = list(s), list(t)
    s_sorted.sort(), t_sorted.sort()

    return True if s_sorted == t_sorted else False

    # for i in range(len(s)):
    #     if s_sorted[i] is not t_sorted[i]:
    #         return False

    # return True


# Approach 2: Hash Table
# time: O(n) - accessing counter is constant time
# space: O(1) - although we do use extra space, the hash table's size
#               stays constant no matter how large n is
def isAnagram(s: str, t: str) -> bool:
    if len(s) is not len(t):
        return False

    counts = Counter(s)

    for char in t:
        if char in counts:
            counts[char] -= 1

    for char in counts:
        if counts[char] != 0:
            return False

    return True


test1 = ("anagram", "nagaram")  # True
test2 = ("rat", "car")  # False

# Discussion Solutions:
def isAnagram(s: str, t: str) -> bool:
    return all(s.count(x) == t.count(x) for x in "abcdefghijklmnopqrstuvwxyz")


def isAnagram(s: str, t: str) -> bool:
    return True if sorted(s) == sorted(t) else False


def test(*args):
    count = 1

    def run():
        for test in args:
            s, t = test
            result = isAnagram(s, t)
            nonlocal count
            print(f"test {count}")
            print(f"result {count}: {result}")
            count += 1

    return run()


test(test1, test2)
