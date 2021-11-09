##
#### Calculator Scraps
###################################################

from collections import deque
import operator


class Calculator(object):
    def evaluate(self, string):
        #operations = {
        #    '+': lambda a, b: a + b,
        #    '-': lambda a, b: a - b,
        #    '*': lambda a, b: a * b,
        #    '/': lambda a, b: a // b,
        #}
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.floordiv,
        }
        
        if len(string) == 1:
            return int(string)
        
        arr = string.split()
        stack = []
        i = 0

        while i < len(arr):
            if arr[i] == '(':
                parens = [arr[i]]
                j = i + 1

                while parens:
                    if arr[j] == '(':
                        parens.append(arr[j])
                    if arr[j] == ')':
                        parens.pop()
                    j += 1

                stack.append(str(self.evaluate(' '.join(arr[i + 1:j - 1]))))
                i = j - 1

            else:
                stack.append(arr[i])

            i += 1

        def helper(operators):
            k = 1

            while k < len(stack) - 1:
                if stack[k] in operators:
                    op = operations[stack[k]]
                    a = int(stack[k - 1])
                    b = int(stack[k + 1])

                    stack[k - 1] = str(op(a, b))
                    stack.pop(k)
                    stack.pop(k)
                    continue

                k += 1

        helper('*/')
        helper('+-')

        return int(stack[0])



## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Calculator().evaluate("2 / 2 + 3 * 4 - 6"), 7)
        self.assertEqual(Calculator().evaluate("3 * 4 + 3 * 7 - 6"), 27)
        self.assertEqual(Calculator().evaluate('1 + 1'), 2)
        self.assertEqual(Calculator().evaluate("( ( ( ( 1 ) * 2 ) ) )"), 2)
        self.assertEqual(Calculator().evaluate("( ( ( ( ( ( ( 5 ) ) ) ) ) ) )"), 5)
        self.assertEqual(Calculator().evaluate("2 * ( 2 * ( 2 * ( 2 * 1 ) ) )"), 16)
        self.assertEqual(Calculator().evaluate("3 * ( 4 + 7 ) - 6"), 27)

        self.assertEqual(Calculator().evaluate("1 + 2"), 3)
        #self.assertEqual(Calculator().evaluate("4*5/2"), 10)
        #self.assertEqual(Calculator().evaluate("-5+-8--11*2"), 9)
        #self.assertEqual(Calculator().evaluate("-.32 /.5"), -0.64)
        #self.assertEqual(Calculator().evaluate("(4-2)*3.5"), 7)
        #self.assertEqual(Calculator().evaluate("2+-+-4"), "Syntax Error (or similar)")
        #self.assertEqual(Calculator().evaluate("19 + cinnamon"), "Invalid Input (or similar)")


if __name__ == '__main__':
    unittest.main()

################################################################################

OPS = '+-*/'


class Calculator:
    def evaluate(self, s):
        '''
        Evaluate an expression.
        
        Converts the expression to reverse polish notation
        using the shunting yard algorithm, evaluating each operator
        as it is produced.
        '''
        
        nums = []
        ops, precs = [], []
        
        for token in s.split():
            if token[0].isdigit() or token[0] == '.':
                nums.append(float(token))
            elif token == '(':
                # special case, no need to add precedence
                ops.append('(')
            elif token == ')':
                while ops[-1] != '(':
                    precs.pop()
                    self._evaluate_op(nums, ops.pop())
                ops.pop()
            elif token in OPS:
                # sneaky integer division
                prec = OPS.index(token) // 2
                while ops and ops[-1] != '(' and precs[-1] >= prec:
                    precs.pop()
                    self._evaluate_op(nums, ops.pop())
                ops.append(token)
                precs.append(prec)
        
        for op in reversed(ops):
            self._evaluate_op(nums, op)
        
        return nums[0]
    
    def _evaluate_op(self, nums, op):
        b, a = nums.pop(), nums.pop()
        if op == '+':
            nums.append(a + b)
        elif op == '-':
            nums.append(a - b)
        elif op == '*':
            nums.append(a * b)
        else:
            nums.append(a / b)


################################################################################


class Calculator(object) :
    def evaluate(self, string) :
        dop = { '+' : lambda a, b : a+b,
                '-' : lambda a, b : a-b,
                '*' : lambda a, b : a*b,
                '/' : lambda a, b : a/b}
        exp = string.split()
        nums = [float(i) for i in exp[::2]]
        ops = exp[1::2]
        while len(ops) :
            im = -1
            id = -1
            if '*' in ops : im = ops.index('*')
            if '/' in ops : id = ops.index('/')  
            if im>=0 and id>=0 : i = min(im, id)
            elif im > 0        : i = im
            elif id > 0        : i = id
            else               : i = 0
            nums = nums[:i] + [dop[ops[i]](nums[i], nums[i+1])] + nums[i+2:]
            ops = ops[:i] + ops[i+1:]
        return nums[0]


################################################################################


class Calculator(object):
    def _safe_float(self, val):
        try:
            return float(val)
        except ValueError:
            return val

    def _evaluate(self, string):
        while '(' in string:
            start_pos = string.rfind('(')  # last '('
            end_pos = string.find(')')     # first ')'
            string = string.replace(
                string[start_pos:end_pos + 1],
                self._evaluate(string[start_pos + 1:end_pos]),
                1
            )

        # ok we are working with no braces now
        string = (string.replace('+ ', '+')).replace('- ', '-')
        arr = [self._safe_float(val) for val in string.split(' ')]
        arr = [val for val in arr if val != '']
        while '/' in arr:
            pos = arr.index('/')
            arr[pos - 1: pos + 2] = [arr[pos - 1] / arr[pos + 1]]
        while '*' in arr:
            pos = arr.index('*')
            arr[pos - 1: pos + 2] = [arr[pos - 1] * arr[pos + 1]]

        return str(sum(arr))

    def evaluate(self, string):
        return float(self._evaluate(string))


################################################################################


## preferred version
##############################
class Solution:
	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		# first define a couple helper methods

		# operation helper to perform basic math operations
		def operation(op, second, first):
			if op == "+":
				return first + second
			elif op == "-":
				return first - second
			elif op == "*":
				return first * second
			elif op == "/":  # integer division
				return first // second

		# calculate the relative precedence of the the operators "()" > "*/" > "+="
		# and determine if we want to do a pre-calculation in the stack
		# (when current_op is <= op_from_ops)
		def precedence(current_op, op_from_ops):
			if op_from_ops == "(" or op_from_ops == ")":
				return False
			if (current_op == "*" or current_op == "/") and (op_from_ops == "+" or op_from_ops == "-"):
				return False
			return True

		if not s:
			return 0
		# define two stack: nums to store the numbers and ops to store the operators
		nums, ops = [], []
		i = 0
		while i < len(s):
			c = s[i]
			if c == " ":
				i += 1
				continue
			elif c.isdigit():
				num = int(c)
				while i < len(s) - 1 and s[i + 1].isdigit():
					num = num * 10 + int(s[i + 1])
					i += 1
				nums.append(num)
			elif c == "(":
				ops.append(c)
			elif c == ")":
				# do the math when we encounter a ')' until '('
				while ops[-1] != "(":
					nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
				ops.pop()
			elif c in ["+", "-", "*", "/"]:
				while len(ops) != 0 and precedence(c, ops[-1]):
					nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
				ops.append(c)
			i += 1

		while len(ops) > 0:
			nums.append(operation(ops.pop(), nums.pop(), nums.pop()))

		return nums.pop()


## preferred version 2 (handles negatives)
##############################################
class Solution:
    def calculate(self, s: str) -> int:
        if not s: return 0
        def precedence(c):
            if c in '+-': return 1
            if c in '*/': return 2
            return 0
        
        def operation(c, n2, n1):
            if c == '+': return n1 + n2
            if c == '-': return n1 - n2
            if c == '*': return n1 * n2
            if c == '/': return int(n1//n2)
        
        ops, data, index, prev = [], [], 0, False
        while index < len(s):
            if s[index] == ' ':
                index += 1
                continue
            if s[index].isdigit():
                end = index+1
                while end < len(s) and s[end].isdigit(): end += 1
                data.append(int(s[index:end]))
                index = end
                prev = True
            elif s[index] in '+-*/':
                if not prev: data.append(0)
                while ops and precedence(ops[-1]) >= precedence(s[index]):
                    data.append(operation(ops.pop(), data.pop(), data.pop()))
                ops.append(s[index])
                index += 1
            elif s[index] == '(': 
                ops.append(s[index])
                index += 1
                prev = False
            else:
                while ops[-1] != '(': 
                    data.append(operation(ops.pop(), data.pop(), data.pop()))
                ops.pop()
                index += 1
        while ops: data.append(operation(ops.pop(), data.pop(), data.pop()))
        return data[-1]


################################################################################

class Solution:
    def calculate(self, s: str) -> int:
        if not s: return 0

        def precedence(c):
            if c in '+-': return 1
            if c in '*/': return 2
            return 0
        
        def operation(a, b, op):
            if c == '+': return a + b
            if c == '-': return a - b
            if c == '*': return a * b
            if c == '/': return int(a / b)
        
        ops = []
        nums = []
        prev = False
        i = 0

        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue

            if s[i].isdigit():
                curr_num = ''

                while i < len(s) and s[i].isdigit():
                    curr_num += s[i]
                    i += 1

                nums.append(int(curr_num))
                curr_num = ''
                prev = True

            elif s[i] in '+-*/':
                if not prev:
                    nums.append(0)

                while ops and precedence(ops[-1]) >= precedence(s[i]):
                    b, a, op = nums.pop(), nums.pop(), ops.pop()
                    nums.append(operation(a, b, op))
                ops.append(s[i])
                i += 1

            elif s[i] == '(': 
                ops.append(s[i])
                i += 1
                prev = False

            else:
                while ops[-1] != '(': 
                    b, a, op = nums.pop(), nums.pop(), ops.pop()
                    nums.append(operation(a, b, op))
                ops.pop()
                i += 1

        while ops:
            b, a, op = nums.pop(), nums.pop(), ops.pop()
            nums.append(operation(a, b, op))

        return nums[-1]

################################################################################
