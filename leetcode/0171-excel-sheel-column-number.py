##
#### Excel Sheet Column Number (easy)
#########################################

# Given a string columnTitle that represents the column title as
# appear in an Excel sheet, return its corresponding column number.

# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...

# Example 1:
# Input: columnTitle = "A"
# Output: 1

# Example 2:
# Input: columnTitle = "AB"
# Output: 28

# Example 3:
# Input: columnTitle = "ZY"
# Output: 701

# Example 4:
# Input: columnTitle = "FXSHRXW"
# Output: 2147483647

# Constraints:
# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"].

#########################################################################

# right to left
def titleToNumber(columnTitle: str) -> int:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_map = {alphabet[i]: i + 1 for i in range(26)}
    count = 0

    length = len(columnTitle)
    for i in range(length):
        current = columnTitle[-1 - i]
        count += alpha_map[current] * (26 ** i)

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


## LeetCode Solutions
#########################


## Approach 1: Right to Left
################################
# time: O(n) - n is number of characters in input string
# space: O(1) - alphabet map is insignificant. No additional memory used
class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0

        # Decimal 65 in ASCII corresponds to char 'A'
        alpha_map = {chr(i + 65): i + 1 for i in range(26)}

        n = len(s)
        for i in range(n):
            cur_char = s[n - 1 - i]
            result += alpha_map[cur_char] * (26 ** i)
        return result


## Approach 2: Left to Right
################################
# time: O(n) -
# space: O(1) -
class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        n = len(s)
        for i in range(n):
            result = result * 26
            result += ord(s[i]) - ord("A") + 1
        return result
