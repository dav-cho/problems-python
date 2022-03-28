##
#### 225. Implement Stack using Queues (easy)
#################################################


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
print(myStack.top())  # return 2
print(myStack.pop())  # return 2
print(myStack.empty())  # return False
print(list(myStack.queue))
print(list(myStack.temp))
