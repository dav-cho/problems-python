##
#### 232. Implement Queue using Stacks (easy)
#################################################


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
myQueue.push(1)  # queue is: [1]
myQueue.push(2)  # queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek()  # return 1
myQueue.pop()  # return 1, queue is [2]
myQueue.empty()  # return false
