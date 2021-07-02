##
#### Roman to Integer (easy)
################################

# Roman numerals are represented by seven
# different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just
# two one's added together. 12 is written as XII, which is simply
# X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from
# left to right. However, the numeral for four is not IIII.
# Instead, the number four is written as IV. Because the one is
# before the five we subtract it making four. The same principle
# applies to the number nine, which is written as IX. There are
# six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

# Given a roman numeral, convert it to an integer.

# Example 1:
# Input: s = "III"
# Output: 3

# Example 2:
# Input: s = "IV"
# Output: 4

# Example 3:
# Input: s = "IX"
# Output: 9

# Example 4:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 5:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

#############################################################################

numerals = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "XC": 90,
    "L": 50,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
}


def romanToInt(s: str) -> int:
    count = 0
    i = 0

    while i < len(s):
        if i is len(s) - 1:
            count += numerals[s[i]]
            i += 1
        else:
            subtractive = s[i] + s[i + 1]
            if subtractive in numerals:
                count += numerals[subtractive]
                i += 2
            else:
                count += numerals[s[i]]
                i += 1

    return count


# Approach 1: Left-to-Right Pass
# time: O(1) - there is a finite set of roman numerals - the max
#              number can be 3999 (MMMCMXCIX)
# space: O(1) - only a constant number of single-value variables are used
values = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,
}


def romanToInt(s: str) -> int:
    total = 0
    i = 0

    while i < len(s):
        if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
            total += values[s[i + 1]] - values[s[i]]
            i += 2
        else:
            total += values[s[i]]
            i += 1

    return total


# Approach 2: Left-to-Right Pass Improved
# time: O(1) - same as Approach 1
# space: O(1) - same as Approach 1
values = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "XC": 90,
    "L": 50,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
}


def romanToInt(s: str) -> int:
    total = 0
    i = 0

    while i < len(s):
        if i < len(s) - 1 and s[i : i + 2] in values:
            total += values[s[i : i + 2]]
            i += 2
        else:
            total += values[s[i]]
            i += 1

    return total


# Approach 3: Right-to-Left Pass
values = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,
}


def romanToInt(s: str) -> int:
    total = values.get(s[-1])

    for i in reversed(range(len(s) - 1)):
        if values[s[i]] < values[s[i + 1]]:
            total -= values[s[i]]
        else:
            total += values[s[i]]

    return total


tests = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
#          3     4     9      58       1994


def test(arr):
    count = 0

    def run():
        for test in arr:
            nonlocal count
            count += 1
            result = romanToInt(test)
            print(f"test {count}")
            print(f"result {count}: {result}")

    return run()


test(tests)
