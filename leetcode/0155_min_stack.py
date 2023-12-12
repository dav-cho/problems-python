##
#### 155. Min Stack (easy)
########################################


## stack with min/value pairs
#################################
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            curr_min = val
        else:
            curr_min = min(self.stack[-1][1], val)
            
        self.stack.append((val, curr_min))

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


## two stacks
##############################
class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        if not self.mins:
            self.mins.append(val)
        elif val <= self.mins[-1]:
            self.mins.append(val)
            
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.mins[-1]:
            self.mins.pop()
            
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]


class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val)
        
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.mins[-1]:
            self.mins.pop()
            
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]


## improved two stacks
##############################
class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        if not self.mins or val < self.mins[-1][0]:
            self.mins.append([val, 1])
        elif val == self.mins[-1][0]:
            self.mins[-1][1] += 1
        
        self.stack.append(val)

    def pop(self) -> None:
        if self.mins[-1][0] == self.stack[-1]:
            self.mins[-1][1] -= 1
        if self.mins[-1][1] == 0:
            self.mins.pop()
        
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1][0]


## first attempt
##############################
class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        if self.mins:
            self.mins.append(min(self.min[-1], val))
        else:
            self.mins.append(val)
            
        self.stack.append(val)

    def pop(self) -> None:
        self.mins.pop()
        
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )


if __name__ == "__main__":
    unittest.main()

