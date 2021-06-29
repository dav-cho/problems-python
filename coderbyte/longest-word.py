##
#### Longest Word
#####################

# Have the function LongestWord(sen) take the sen parameter being passed
# and return the longest word in the string. If there are two or more words
# that are the same length, return the first word from the string with
# that length. Ignore punctuation and assume sen will not be empty.
# Words may also contain numbers, for example "Hello world123 567"

# Examples:
# Input: "fun&!! time"
# Output: time
# Input: "I love dogs"
# Output: love

##############################################################################

import re


# def longest_word(sen: str) -> str:
#     pattern = re.compile(r"\W+")
#     x = pattern.split(sen)
#     return max(x, key=len)


# def longest_word(sen: str) -> str:
#     words = ""
#     for letter in sen:
#         if letter.isalpha() or letter.isnumeric():
#             words += letter
#         else:
#             words += " "
#     return max(words.split(), key=len)


longest_word1 = longest_word("fun&!! time")  # time
longest_word2 = longest_word("I love dogs")  # love
print(longest_word1)
print(longest_word2)
