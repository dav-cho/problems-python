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

# "Fizz" --> i % 3 = 0
# "Buzz" --> i % 5 = 0
# "FizzBuzz" --> i % 3 and i % 5 = 0


# Approach 2: String Concatenation
def fizzBuzz(n: int) -> list[str]:
    result = []

    for i in range(1, n + 1):
        div_3 = i % 3 == 0
        div_5 = i % 5 == 0
        result_str = ""

        if div_3:
            result_str += "Fizz"
        if div_5:
            result_str += "Buzz"
        if not result_str:
            result_str = str(i)

        result.append(result_str)

    return result


# Approach 3: Hash
def fizzBuzz(n: int) -> list[str]:
    hash = {3: "Fizz", 5: "Buzz"}
    result = []

    for i in range(1, n + 1):
        result_str = ""

        for key in hash.keys():
            if i % key == 0:
                result_str += hash[key]

        if not result_str:
            result_str = str(i)

        result.append(result_str)

    return result


tests = [3, 5, 15]
# 3: ["1","2","Fizz"]
# 5: ["1","2","Fizz","4","Buzz"]
# 15: ["1","2","Fizz","4","Buzz","Fizz","7","8",
#      "Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]


def test(arr):
    count = 0

    def run():
        for test in arr:
            nonlocal count
            count += 1
            result = fizzBuzz(test)
            print(f"test: {count}")
            print(f"result {count}: {result}")

    return run()


test(tests)
