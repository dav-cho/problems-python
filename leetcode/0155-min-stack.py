##
#### Min Stack (easy)
########################################

# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
 
# Example 1:
# Input:
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# Output:
# [null,null,null,null,-3,null,0,-2]
# Explanation:
# minStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

# constraints:
# -231 <= val <= 231 - 1
# methods pop, top and getMin operations will always be called on non-empty stacks.
# at most 3 * 104 calls will be made to push, pop, top, and getMin.

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

################################################################################

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


## LeetCode Solutions
#########################

## Approach 1: Stack of Value/ Minimum Pairs
################################################
# Time: O(1) - For all operations.
# - push(...): Checking the top of a Stack, comparing numbers, and pushing to
#              the top of a Stack (or adding to the end of an Array or List)
#              are all O(1) operations. Therefore, this overall is an O(1)
#              operation.
# - pop(...): Popping from a Stack (or removing from the end of an Array, or
#             List) is an O(1) operation.
# - top(...): Looking at the top of a Stack is an O(1) operation.
# - getMin(...): Same as above. This operation is O(1) because we do not need
#                to compare values to find it. If we had not kept track of it
#                on the Stack, and instead had to search for it each time, the
#                overall time complexity would have been O(n).

# Space: O(n)
# - Worst case is that all the operations are push. In this case, there will be
#   O(2⋅n)=O(n) space used.

class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        
        # If the stack is empty, then the min value
        # must just be the first value we add
        if not self.stack:
            self.stack.append((x, x))
            return

        current_min = self.stack[-1][1]
        self.stack.append((x, min(x, current_min)))
        
        
    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]


## Approach 2: Two Stacks
##############################
# Time: O(1) - Same as above. All our modifications are still O(1).
# Space: O(n) - Same as above.
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []        
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    
    def pop(self) -> None:
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


## Approach 3: Improved Two Stacks
######################################
# Time: O(1) - For all operations. Same as above.
# Space: O(n) - Same as above.
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []        
        

    def push(self, x: int) -> None:
        
        # We always put the number onto the main stack.
        self.stack.append(x)
        
        # If the min stack is empty, or this number is smaller than
        # the top of the min stack, put it on with a count of 1.
        if not self.min_stack or x < self.min_stack[-1][0]:
            self.min_stack.append([x, 1])
            
        # Else if this number is equal to what's currently at the top
        # of the min stack, then increment the count at the top by 1.
        elif x == self.min_stack[-1][0]:
            self.min_stack[-1][1] += 1

    
    def pop(self) -> None:

        # If the top of min stack is the same as the top of stack
        # then we need to decrement the count at the top by 1.
        if self.min_stack[-1][0] == self.stack[-1]:
            self.min_stack[-1][1] -= 1
            
        # If the count at the top of min stack is now 0, then remove
        # that value as we're done with it.
        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()
            
        # And like before, pop the top of the main stack.
        self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.min_stack[-1][0]


