##
#### Implement Queue Using Stacks (easy)
############################################

# Implement a first in first out (FIFO) queue using only two stacks.
# The implemented queue should support all the functions of a normal
# queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push
# to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively.
# You may simulate a stack using a list or deque (double-ended queue)
# as long as you use only a stack's standard operations.
# Follow-up: Can you implement the queue such that each operation is
# amortized O(1) time complexity? In other words, performing n operations
# will take overall O(n) time even if one of those operations may take longer.

# Example 1:
# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false


# Constraints:
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, peek, and empty.
# All the calls to pop and peek are valid.

#################################################################################


class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop(0)

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return not self.stack


# Approach 1: Two Stacks
# ----------------------
# push - O(N) per operation
# pop - O(1) per operation
class MyQueue:
    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, x: int) -> None:
        while self.stack:
            self.temp.append(self.stack.pop())
        self.stack.append(x)
        while self.temp:
            self.stack.append(self.temp.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not self.stack


# Approach 2: Two Stacks
# ----------------------
# push - O(1) per operation
# pop - Amortized O(1) per operation
class MyQueue:
    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self.peek()
        return self.temp.pop()

    def peek(self) -> int:
        if not self.temp:
            while self.stack:
                self.temp.append(self.stack.pop())
        return self.temp[-1]

    def empty(self) -> bool:
        return not self.stack and not self.temp2


my_queue = MyQueue()

my_queue.push(1)  # queue is: [1]
print(my_queue.stack)

my_queue.push(2)  # queue is: [1, 2] (leftmost is front of the queue)
print(my_queue.stack)

peek1 = my_queue.peek()  # return 1
print("~ peek1", peek1)

popped1 = my_queue.pop()  # return 1, queue is [2]
print("~ popped1", popped1)
print(my_queue.stack)

is_empty = my_queue.empty()  # return false
print("~ is_empty", is_empty)
