##
#### 150. Evaluate Reverse Polish Notation (medium)
#######################################################


## first try
################
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
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
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
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
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
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
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
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
