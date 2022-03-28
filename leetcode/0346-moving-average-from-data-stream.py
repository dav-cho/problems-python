##
#### 346. Moving Average from Data Stream (easy)
####################################################


## attempt 1
######################
from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.queue = deque()
        self.capacity = size
        self.size = 0

    def next(self, val: int) -> float:
        if self.size == self.capacity:
            self.queue.popleft()
            self.size -= 1

        self.queue.append(val)
        self.size += 1

        return sum(self.queue) / self.size


## queue
############
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        self.queue.append(val)

        return sum(self.queue[-self.size :]) / min(len(self.queue), self.size)


## double ended queue
#########################
from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.queue = deque()
        self.capacity = size
        self.size = 0
        self.sum = 0

    def next(self, val: int) -> float:
        self.size += 1
        self.queue.append(val)
        tail = self.queue.popleft() if self.size > self.capacity else 0
        self.sum = self.sum - tail + val

        return self.sum / min(self.size, self.capacity)


class MovingAverage:
    def __init__(self, size: int):
        self.queue = deque(maxlen=size)

    def next(self, val: int) -> float:
        self.queue.append(val)
        return sum(queue) / len(queue)


## circular queue with array
################################
class MovingAverage:
    def __init__(self, size: int):
        self.capacity = size
        self.queue = [0] * size
        self.head = 0
        self.size = 0
        self.sum = 0

    def next(self, val: int) -> float:
        self.size += 1
        tail = (self.head + 1) % self.capacity
        self.sum = self.sum - self.queue[tail] + val
        self.head = (self.head + 1) % self.capacity
        self.queue[self.head] = val

        return self.sum / min(self.size, self.capacity)


class MovingAverage:
    def __init__(self, size: int):
        self.capacity = size
        self.queue = [None] * size
        self.head = 0
        self.size = 0
        self.sum = 0

    def next(self, val: int) -> float:
        if self.size == self.capacity:
            self.sum -= self.queue[self.head]
            self.queue[self.head] = val
            self.head = (self.head + 1) % self.capacity
        else:
            tail = (self.head + self.size) % self.capacity
            self.queue[tail] = val
            self.size += 1
        self.sum += val

        return self.sum / min(self.size, self.capacity)


## Tests
#############

# movingAverage = MovingAverage(3)
# print(movingAverage.next(1))		# 1.0 = 1 / 1
# print(movingAverage.next(10))		# 5.5 = (1 + 10) / 2
# print(movingAverage.next(3))		# 4.66667 = (1 + 10 + 3) / 3
# print(movingAverage.next(5))		# 6.0 = (10 + 3 + 5) / 3

movingAverage = MovingAverage(5)
print(movingAverage.next(12009))  # 12009.00000
print(movingAverage.next(1965))  # 6987.00000
print(movingAverage.next(-940))  # 4344.66667
print(movingAverage.next(-8516))  # 1129.50000
print(movingAverage.next(-16446))  # -2385.60000
print(movingAverage.next(7870))  # -3213.40000
print(movingAverage.next(25545))  # 1502.60000
print(movingAverage.next(-21028))  # -2515.00000
print(movingAverage.next(18430))  # 2874.20000
print(movingAverage.next(-2364))  # 5690.60000
