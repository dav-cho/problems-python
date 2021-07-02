##
#### Reverse String (easy)
##############################

# Write a function that reverses a string.
# The input string is given as an array of characters s.


# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# Constraints:
# 1 <= s.length <= 105
# s[i] is a printable ascii character.

# Follow up: Do not allocate extra space for another array.
# You must do this by modifying the input array in-place with O(1) extra memory.

#################################################################################


def reverseString(s: list[int]) -> None:
    start = 0
    end = len(s) - 1

    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1

    print(s)


test1 = ["h", "e", "l", "l", "o"]
test2 = ["H", "a", "n", "n", "a", "h"]


def test(*args):
    count = 0

    def run():
        for test in args:
            nonlocal count
            count += 1
            print(f"test {count}")
            reverseString(test)

    return run()


test(test1, test2)
