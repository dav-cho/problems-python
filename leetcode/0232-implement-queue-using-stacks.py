##
#### Implement Queue using Stacks (easy)
############################################

# Implement a first in first out (FIFO) queue using only two stacks. The
# implemented queue should support all the functions of a normal queue (push,
# peek, pop, and empty).

# Implement the MyQueue class:
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.

# Notes:
# You must use only standard operations of a stack, which means only push to
# top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may
# simulate a stack using a list or deque (double-ended queue) as long as you use
# only a stack's standard operations.
#
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

################################################################################

## 
##############################
class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []
        
    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self.peek()
        return self.output.pop()

    def peek(self) -> int:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output


class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        while self.output:
            self.input.append(self.output.pop())
        self.input.append(x)

    def pop(self) -> int:
        while self.input:
            self.output.append(self.input.pop())
        return self.output.pop()

    def peek(self) -> int:
        while self.input:
            self.output.append(self.input.pop())
        return self.output[-1]
        
    def empty(self) -> bool:
        return not self.input and not self.output


## Tests
#############

myQueue = MyQueue()
myQueue.push(1)         # queue is: [1]
myQueue.push(2)         # queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek()          # return 1
myQueue.pop()           # return 1, queue is [2]
myQueue.empty()         # return false

## LeetCode Solutions
#########################

## Approach 1: (Two Stacks)
###############################
# Time: 
# - Push: O(n) - Each element, with the exception of the newly arrived, is
#                pushed and popped twice. The last inserted element is popped
#                and pushed once.  Therefore this gives 4n + 2 operations where
#                n is the queue size. The push and pop operations have O(1)
#                time complexity.
# - Pop: O(1)
# - Empty: O(1)
# - Peek: O(1) - The front element has been calculated in advance and only
#                returned in peek operation.

# Space: 
# - Push: O(n) - We need additional memory to store the queue elements
# - Pop: O(1)
# - Empty: O(1)
# - Peek: O(1)

## Java
#private int front;
#
#public void push(int x) {
#    if (s1.empty())
#        front = x;
#    while (!s1.isEmpty())
#        s2.push(s1.pop());
#    s2.push(x);
#    while (!s2.isEmpty())
#        s1.push(s2.pop());
#}
#
#public void pop() {
#    s1.pop();
#    if (!s1.empty())
#        front = s1.peek();
#}
#
#public boolean empty() {
#    return s1.isEmpty();
#}
#
#// Get the front element.
#public int peek() {
#  return front;
#}


## Approach 2: (Two Stacks)
###############################
# Time: 
# - Push: O(1) - Аppending an element to a stack is an O(1) operation.
# - Pop: Amortized O(1)
#        Worse-case O(n) 
#        - In the worst case scenario when stack s2 is empty, the algorithm pops
#          n elements from stack s1 and pushes nn elements to s2, where n is the
#          queue size. This gives 2n operations, which is O(n). But when stack
#          s2 is not empty the algorithm has O(1) time complexity. So what does
#          it mean by Amortized O(1)? Please see the next section on Amortized
#         Analysis for more information.
# - Empty: O(1)
# - Peek: O(1) - The front element was either previously calculated or returned
#                as a top element of stack s2. Therefore complexity is O(1).

# Space: 
# - Push: O(n) - We need additional memory to store the queue elements
# - Pop: O(1)
# - Empty: O(1)
# - Peek: O(1)

#private Stack<Integer> s1 = new Stack<>();
#private Stack<Integer> s2 = new Stack<>();
#
#// Push element x to the back of queue.
#public void push(int x) {
#    if (s1.empty())
#        front = x;
#    s1.push(x);
#}
#
#// Removes the element from in front of queue.
#public void pop() {
#    if (s2.isEmpty()) {
#        while (!s1.isEmpty())
#            s2.push(s1.pop());
#    }
#    s2.pop();    
#}
#
#// Return whether the queue is empty.
#public boolean empty() {
#    return s1.isEmpty() && s2.isEmpty();
#}
#
#// Get the front element.
#public int peek() {
#    if (!s2.isEmpty()) {
#            return s2.peek();
#    }
#    return front;
#}




## Approach 3: 
###################
# Time: 
# Space: 


