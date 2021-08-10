##
#### Evaluate Reverse Polish Notation (medium)
##################################################

# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, and /. Each operand may be an integer or another
# expression.

# Note that division between two integers should truncate toward zero.

# It is guaranteed that the given RPN expression is always valid. That means
# the expression would always evaluate to a result, and there will not be any
# division by zero operation.

# Example 1:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Example 2:
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

# Example 3:
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
 
# Constraints:
# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

################################################################################

## first try
################
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }
        
        operation = None
        stack = []
        for char in tokens:
            if char in operations:
                operation = operations[char]
            else:
                stack.append(char)
            
            if operation:
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(operation(a, b))
                operation = None
                
        return stack[0]


## reduce list in place
###########################
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }
        
        position = 0
        while len(tokens) > 1:
            while tokens[position] not in operations:
                position += 1
                
            a = int(tokens[position - 2])
            b = int(tokens[position - 1])
            operation = operations[tokens[position]]
            tokens[position] = operation(a, b)
            
            tokens.pop(position - 2)
            tokens.pop(position - 2)
            position -= 1
            
        return tokens[0]


## using stack
##################
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),
        }
        
        stack = []
        for token in tokens:
            if token in operations:
                b = stack.pop()
                a = stack.pop()
                stack.append(operations[token](a, b))
            else:
                stack.append(int(token))
                
        return stack[0]


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }
        
        stack = []
        for token in tokens:
            if token in operations:
                b = stack.pop()
                a = stack.pop()
                operation = operations[token]
                stack.append(operation(a, b))
            else:
                stack.append(int(token))
                
        return stack.pop()


## Tests
#############


## LeetCode Solutions
#########################

## Approach 1: Reducing the List In-place
#############################################
# Time: O(n^2)
# Firstly, it helps to calculate how many operators and how many numbers are in
# the initial list. Each step of the algorithm removes 1 operator, 2 numbers,
# and adds back 1 number. This is an overall loss of 1 number and 1 operator
# per step. At the end, we have 1 number left. Therefore, we can infer that at
# the start, there must always be exactly 1 more number than there is operators.

# The big inefficiency of this approach is more obvious in the Java code than
# the Python. Deleting an item from an ArrayList or Array is O(n), because all
# the items after have to be shuffled down one place to fill in the gap. The
# number of these deletions we need to do is the same as the number of
# operators, which is proportional to n. Therefore, the cost of the deletions
# is O(n^2)

# This is more obvious in the Java code, because we had to define the deletion
# method ourselves. However, the Python deletion method works the same way, it's
# just that you can't see it because it's hidden in a library function call.
# It's important to always be aware of the cost of library functions as they can
# sometimes look like they're O(1) when they're not!

# Space: O(1)
# The only extra space used is a constant number of single-value variables.
# Therefore, the overall algorithm requires O(1) space.
def evalRPN(self, tokens: List[str]) -> int:

        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b
        }
        
        current_position = 0
        
        while len(tokens) > 1:
            
            # Move the current position pointer to the next operator.
            while tokens[current_position] not in "+-*/":
                current_position += 1
        
            # Extract the operator and numbers from the list.
            operator = tokens[current_position]
            number_1 = int(tokens[current_position - 2])
            number_2 = int(tokens[current_position - 1])
            
            # Calculate the result to overwrite the operator with.
            operation = operations[operator]
            tokens[current_position] = operation(number_1, number_2)
            
            # Remove the numbers and move the pointer to the position
            # after the new number we just added.
            tokens.pop(current_position - 2)
            tokens.pop(current_position - 2)
            current_position -= 1
        
        return tokens[0]


## Approach 2: Evaluate with Stack
######################################
# Time: O(n)
# We do a linear search to put all numbers on the stack, and process all
# operators. Processing an operator requires removing 2 numbers off the stack
# and replacing them with a single number, which is an O(1) operation.
# Therefore, the total cost is proportional to the length of the input array.
# Unlike before, we're no longer doing expensive deletes from the middle of an
# Array or List.

# Space: O(n)
# In the worst case, the stack will have all the numbers on it at the same time.
# This is never more than half the length of the input array.
def evalRPN(self, tokens: List[str]) -> int:
        
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: int(a / b),
        "*": lambda a, b: a * b
    }
    
    stack = []
    for token in tokens:
        if token in operations:
            number_2 = stack.pop()
            number_1 = stack.pop()
            operation = operations[token]
            stack.append(operation(number_1, number_2))
        else:
            stack.append(int(token))
    return stack.pop()


