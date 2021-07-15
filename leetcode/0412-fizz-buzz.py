##
#### Fizz Buzz (easy)
#########################

# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i if non of the above conditions are true.


# Example 1:
# Input: n = 3
# Output: ["1","2","Fizz"]

# Example 2:
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]

# Example 3:
# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8",
#          "Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

# Constraints:
# 1 <= n <= 104

#################################################################

## Approach 1: Naive Approach
#################################
# time: O(n)
# space: O(1)
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        pass


## Approach 2: String Concatenation
#######################################
# time: O(n)
# space: O(1)
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        pass


## Approach 3: Hash it!
###########################
# time: O(n)
# space: O(1)
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        pass


## Tests
############
def test(arr):
    solution = Solution()
    count = 0

    def run():
        for test in arr:
            nonlocal count
            count += 1
            result = solution.fizzBuzz(test)
            print(f"test: {count}")
            print(f"result {count}: {result}")

    return run()


tests = [3, 5, 15]
# 3: ["1","2","Fizz"]
# 5: ["1","2","Fizz","4","Buzz"]
# 15: ["1","2","Fizz","4","Buzz","Fizz","7","8",
#      "Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

test(tests)


## LeetCode Solutions
#########################


## Approach 1: Naive Approach
#################################
# time: O(n)
# space: O(1)
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # ans list
        ans = []

        for num in range(1, n + 1):

            divisible_by_3 = num % 3 == 0
            divisible_by_5 = num % 5 == 0

            if divisible_by_3 and divisible_by_5:
                # Divides by both 3 and 5, add FizzBuzz
                ans.append("FizzBuzz")
            elif divisible_by_3:
                # Divides by 3, add Fizz
                ans.append("Fizz")
            elif divisible_by_5:
                # Divides by 5, add Buzz
                ans.append("Buzz")
            else:
                # Not divisible by 3 or 5, add the number
                ans.append(str(num))

        return ans


## Approach 2: String Concatenation
#######################################
# time: O(n)
# space: O(1)
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # ans list
        ans = []

        for num in range(1, n + 1):

            divisible_by_3 = num % 3 == 0
            divisible_by_5 = num % 5 == 0

            num_ans_str = ""

            if divisible_by_3:
                # Divides by 3
                num_ans_str += "Fizz"
            if divisible_by_5:
                # Divides by 5
                num_ans_str += "Buzz"
            if not num_ans_str:
                # Not divisible by 3 or 5
                num_ans_str = str(num)

            # Append the current answer str to the ans list
            ans.append(num_ans_str)

        return ans


## Approach 3: Hash it!
###########################
# time: O(n)
# space: O(1)
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # ans list
        ans = []

        # Dictionary to store all fizzbuzz mappings
        fizz_buzz_dict = {3: "Fizz", 5: "Buzz"}

        for num in range(1, n + 1):

            num_ans_str = ""

            for key in fizz_buzz_dict.keys():

                # If the num is divisible by key,
                # then add the corresponding string mapping to current num_ans_str
                if num % key == 0:
                    num_ans_str += fizz_buzz_dict[key]

            if not num_ans_str:
                num_ans_str = str(num)

            # Append the current answer str to the ans list
            ans.append(num_ans_str)

        return ans
