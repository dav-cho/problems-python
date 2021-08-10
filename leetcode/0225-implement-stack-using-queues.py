##
#### Implement Stack using Queues (easy)
############################################

# Implement a last-in-first-out (LIFO) stack using only two queues. The
# implemented stack should support all the functions of a normal stack (push,
# top, pop, and empty).

# Implement the MyStack class:
# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.

# Notes:
# You must use only standard operations of a queue, which means that only push
# to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may
# simulate a queue using a list or deque (double-ended queue) as long as you
# use only a queue's standard operations.

# Example 1:
# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return Falsee

################################################################################

## one queue (deque)
##############################
import collections

class MyStack:
    def __init__(self):
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


## Tests
#############

myStack = MyStack() 
myStack.push(1) 
myStack.push(2) 
print(myStack.top)
print(myStack.top())           # return 2
print(myStack.pop())           # return 2
print(myStack.empty())         # return False
print(list(myStack.queue))
print(list(myStack.temp))


## LeetCode Solutions
#########################

## Approach 1: (Two Queues, push - O(1), pop O(n))
######################################################
# Time:
# - Push: O(1) - Queue is implemented as linked list and add operation has O(1)
#                time complexity.
# - Pop: O(n) - The algorithm dequeues n elements from q1 and enqueues n - 1
#               elements to q2, where nn is the stack size. This gives 2n - 1
#               operations.

# Space:
# - Push: O(1)
# - Pop: O(1)

## Java
#private Queue<Integer> q1 = new LinkedList<>();
#private Queue<Integer> q2 = new LinkedList<>();
#private int top;
#
#// Push element x onto stack.
#public void push(int x) {
#    q1.add(x);
#    top = x;
#}
#
#// Removes the element on top of the stack.
#public void pop() {
#    while (q1.size() > 1) {
#        top = q1.remove();
#        q2.add(top);
#    }
#    q1.remove();
#    Queue<Integer> temp = q1;
#    q1 = q2;
#    q2 = temp;
#}


## Approach 2: (Two Queues, push - O(n), pop O(1) )
#######################################################
# Time: 
# - Push: O(n) - The algorithm removes n elements from q1 and inserts n + 1
#                elements to q2, where n is the stack size. This gives 2n + 1
#                operations. The operations add and remove in linked lists has
#                O(1) complexity.
# - Pop: O(1)
# - Empty: O(1)
# - Top: O(1) - The top element has been calculated in advance and only returned
#               in top operation.

# Space: 
# - Push: O(1)
# - Pop: O(1)
# - Empty: O(1)
# - Top: O(1)

## Java
#public void push(int x) {
#    q2.add(x);
#    top = x;
#    while (!q1.isEmpty()) {                
#        q2.add(q1.remove());
#    }
#    Queue<Integer> temp = q1;
#    q1 = q2;
#    q2 = temp;
#}
#
#// Removes the element on top of the stack.
#public void pop() {
#    q1.remove();
#    if (!q1.isEmpty()) {
#    	top = q1.peek();
#    }
#}
#
#// Return whether the stack is empty.
#public boolean empty() {
#    return q1.isEmpty();
#}
#
#// Get the top element.
#public int top() {
#    return top;
#}


## Approach 3: (One Queue, push - O(n), pop O(1))
#####################################################
# Time:
# Push: O(n) - The algorithm removes n elements and inserts n + 1 elements to
#              q1 , where n is the stack size. This gives 2n + 1 operations. The
#              operations add and remove in linked lists has O(1) complexity.
# Pop: O(1)
# Empty: O(1)
# Top: O(1)

# Space: 
# Push: O(1)
# Pop: O(1)
# Empty: O(1)
# Top: O(1)

## Java
#private LinkedList<Integer> q1 = new LinkedList<>();
#
#// Push element x onto stack.
#public void push(int x) {
#    q1.add(x);
#    int sz = q1.size();
#    while (sz > 1) {
#        q1.add(q1.remove());
#        sz--;
#    }
#}
#
#// Removes the element on top of the stack.
#public void pop() {
#    q1.remove();
#}
#
#// Return whether the stack is empty.
#public boolean empty() {
#    return q1.isEmpty();
#}
#
#// Get the top element.
#public int top() {
#    return q1.peek();
#}
  

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyStack:
    def __init__(self):
        self.input = ListNode(None)
        self.output = ListNode(None)
        self.size = 0

    def push(self, x: int) -> None:
        curr_in = self.input
        curr_out = self.output
        for _ in range(self.size):
            curr_in.next = curr_out.next
            curr_out.next, curr_out = None, curr_out.next
        
        curr_in.next = ListNode(x)
        self.size += 1
        
    def pop(self) -> int:
        self.size -= 1
        curr_in = self.input
        curr_out = self.output
        for _ in range(self.size):
            curr_out.next = curr_in.next
            curr_in.next, curr_in = None, curr_in.next
        
        val = curr_in.val
        self.input.next = None
        
        return val

    def top(self) -> int:
        if self.input.next:
            return self.input.next.val
        if self.output.next:
            return self.output.next.val

    def empty(self) -> bool:
        return not self.input.next and not self.output.next

################################################################################

class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        
    def top(self) -> int:
        """
        Get the top element.
        """
        
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
