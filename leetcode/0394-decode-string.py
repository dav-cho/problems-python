##
#### Decode String (medium)
###############################

# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.

# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

# Example 4:
# Input: s = "abc3[cd]xyz"
# Output: "abccdccdxyz"
 
# Constraints:
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].d

################################################################################

## single stack
###################
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ']':
                curr = ''
                while stack[-1] != '[':
                    curr = stack.pop() + curr
                
                stack.pop()
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                    
                for _ in range(int(k)):
                    stack.append(curr)
            else:
                stack.append(char)
            
        return ''.join(stack)


## two stacks
#################
class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        str_stack = ['']
        curr_str = ''
        k = ''
        for char in s:
            if char.isdigit():
                k += char
            if char.isalpha():
                curr_str += char
            if char == '[':
                count_stack.append(int(k))
                str_stack.append(curr_str)
                k = ''
                curr_str = ''
            if char == ']':
                curr_str = str_stack.pop() + curr_str * count_stack.pop()
                
        return curr_str


## recursion
################


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.decodeString('3[a]2[b]'), 'aaabb')
        self.assertEqual(solution.decodeString("3[a]2[bc]"), "aaabcbc")
        self.assertEqual(solution.decodeString("3[a2[c]]"), "accaccacc")
        self.assertEqual(solution.decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")
        self.assertEqual(solution.decodeString("abc3[cd]xyz"), "abccdcdcdxyz")


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Using Stack
##############################
# Time: O(maxK^(countK) * n)
# - Where maxK is the maximum value of k, countK is the count of nested k values
#   and n is the maximum length of encoded string. Example, for s = 20[a10[bc]],
#   maxK is 20, countK is 2 as there are 2 nested k values (20 and 10) . Also,
#   there are 2 encoded strings a and bc with maximum length of encoded string,
#   n as 2
# - The worst case scenario would be when there are multiple nested patterns.
#   Let's assume that all the k values (maxK) are 10 and all encoded string(n)
#   are of size 2.
# - For, s = 10[ab10[cd]]10[ef], time complexity would be roughly equivalent to
#   10 ∗ cd ∗ 10 ∗ ab + 10 ∗ 2 = 10^2 ∗ 2.
# - Hence, for an encoded pattern of form maxK[nmaxK[n]], the time complexity to
#   decode the pattern can be given as, O(maxK^countK ⋅n).

# Space: O(sum(maxK^(countK) * n)
# - where maxK is the maximum value of k, countK is the count of nested k values
#   and n is the maximum length of encoded string.

## C++
#class Solution {
#public:
#    string decodeString(string s) {
#        stack<char> stack;
#        for (int i = 0; i < s.length(); i++) {
#            if (s[i] == ']') {
#                string decodedString = "";
#                // get the encoded string
#                while (stack.top() != '[') {
#                    decodedString += stack.top();
#                    stack.pop();
#                }
#                // pop [ from stack
#                stack.pop();
#                int base = 1;
#                int k = 0;
#                // get the number k
#                while (!stack.empty() && isdigit(stack.top())) {
#                    k = k + (stack.top() - '0') * base;
#                    stack.pop();
#                    base *= 10;
#                }
#                int currentLen = decodedString.size();
#                // decode k[decodedString], by pushing decodedString k times into stack
#                while (k != 0) {
#                    for (int j = decodedString.size() - 1; j >= 0; j--) {
#                        stack.push(decodedString[j]);
#                    }
#                    k--;
#                }
#            }
#            // push the current character to stack
#            else {
#                stack.push(s[i]);
#            }
#        }
#        // get the result from stack
#        string result;
#        for (int i = stack.size() - 1; i >= 0; i--) {
#            result = stack.top() + result;
#            stack.pop();
#        }
#        return result;
#    }
#};


## Java
#class Solution {
#    public String decodeString(String s) {
#        Stack<Character> stack = new Stack<>();
#        for (int i = 0; i < s.length(); i++) {
#            if (s.charAt(i) == ']') {
#                List<Character> decodedString = new ArrayList<>();
#                // get the encoded string
#                while (stack.peek() != '[') {
#                    decodedString.add(stack.pop());
#                }
#                // pop [ from the stack
#                stack.pop();
#                int base = 1;
#                int k = 0;
#                // get the number k
#                while (!stack.isEmpty() && Character.isDigit(stack.peek())) {
#                    k = k + (stack.pop() - '0') * base;
#                    base *= 10;
#                }
#                // decode k[decodedString], by pushing decodedString k times into stack
#                while (k != 0) {
#                    for (int j = decodedString.size() - 1; j >= 0; j--) {
#                        stack.push(decodedString.get(j));
#                    }
#                    k--;
#                }
#            }
#            // push the current character to stack
#            else {
#                stack.push(s.charAt(i));
#            }
#        }      
#        // get the result from stack
#        char[] result = new char[stack.size()];
#        for (int i = result.length - 1; i >= 0; i--) {
#            result[i] = stack.pop();
#        }
#        return new String(result);
#    }
#}


## Approach 2: Using 2 Stack
################################
# Time: O(maxK * n) - Assume, n is the length of the string s.
# - Where maxK is the maximum value of k and nn is the length of a given string
#   s. We traverse a string of size n and iterate k times to decode each pattern
#   of form k[string]. This gives us worst case time complexity as O(maxK⋅n).

# Space: O(m + n) - Assume, n is the length of the string s.
# - Where m is the number of letters(a-z) and n is the number of digits(0-9) in
#   string s. In worst case, the maximum size of stringStack and countStack
#   could be m and n respectively.

## C++
#class Solution {
#public:
#    string decodeString(string s) {
#        stack<int> countStack;
#        stack<string> stringStack;
#        string currentString;
#        int k = 0;
#        for (auto ch : s) {
#            if (isdigit(ch)) {
#                k = k * 10 + ch - '0';
#            } else if (ch == '[') {
#                // push the number k to countStack
#                countStack.push(k);
#                // push the currentString to stringStack
#                stringStack.push(currentString);
#                // reset currentString and k
#                currentString = "";
#                k = 0;
#            } else if (ch == ']') {
#                string decodedString = stringStack.top();
#                stringStack.pop();
#                // decode currentK[currentString] by appending currentString k times
#                for (int currentK = countStack.top(); currentK > 0; currentK--) {
#                    decodedString = decodedString + currentString;
#                }
#                countStack.pop();
#                currentString = decodedString;
#            } else {
#                currentString = currentString + ch;
#            }
#        }
#        return currentString;
#    }
#};

## Java
#class Solution {
#    String decodeString(String s) {
#        Stack<Integer> countStack = new Stack<>();
#        Stack<StringBuilder> stringStack = new Stack<>();
#        StringBuilder currentString = new StringBuilder();
#        int k = 0;
#        for (char ch : s.toCharArray()) {
#            if (Character.isDigit(ch)) {
#                k = k * 10 + ch - '0';
#            } else if (ch == '[') {
#                // push the number k to countStack
#                countStack.push(k);
#                // push the currentString to stringStack
#                stringStack.push(currentString);
#                // reset currentString and k
#                currentString = new StringBuilder();
#                k = 0;
#            } else if (ch == ']') {
#                StringBuilder decodedString = stringStack.pop();
#                // decode currentK[currentString] by appending currentString k times
#                for (int currentK = countStack.pop(); currentK > 0; currentK--) {
#                    decodedString.append(currentString);
#                }
#                currentString = decodedString;
#            } else {
#                currentString.append(ch);
#            }
#        }
#        return currentString.toString();
#    }
#}


## Approach 3: Using Recursion
##################################
# Time: O(maxK * n) - As in Approach 2
# Space: O(n) - This is the space used to store the internal call stack used for
#               recursion. As we are recursively decoding each nested pattern,
#               the maximum depth of recursive call stack would not be more
#               than n.

## C++
#class Solution {
#public:
#    string decodeString(string s) {
#        int index = 0;
#        return decodeString(s, index);
#    }
#    string decodeString(const string& s, int& index) {
#        string result;
#        while (index < s.length() && s[index] != ']') {
#            if (!isdigit(s[index]))
#                result += s[index++];
#            else {
#                int k = 0;
#                // build k while next character is a digit
#                while (index < s.length() && isdigit(s[index]))
#                    k = k * 10 + s[index++] - '0';  
#                // ignore the opening bracket '['    
#                index++;
#                string decodedString = decodeString(s, index);
#                // ignore the closing bracket ']'
#                index++;        
#                while (k-- > 0)
#                    result += decodedString;
#            }
#        }
#        return result;
#    }
#};

## Java
#class Solution {
#    int index = 0;
#    String decodeString(String s) {
#        StringBuilder result = new StringBuilder();
#        while (index < s.length() && s.charAt(index) != ']') {
#            if (!Character.isDigit(s.charAt(index)))
#                result.append(s.charAt(index++));
#            else {
#                int k = 0;
#                // build k while next character is a digit
#                while (index < s.length() && Character.isDigit(s.charAt(index)))
#                    k = k * 10 + s.charAt(index++) - '0';
#                // ignore the opening bracket '['    
#                index++;
#                String decodedString = decodeString(s);
#                // ignore the closing bracket ']'
#                index++;
#                / build k[decodedString] and append to the result
#                while (k-- > 0)
#                    result.append(decodedString);
#            }
#        }
#        return new String(result);
#    }
#}

