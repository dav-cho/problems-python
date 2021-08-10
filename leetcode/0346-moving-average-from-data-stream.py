##
#### Moving Average from Data Stream (easy)
###############################################

# Given a stream of integers and a window size, calculate the moving average of
# all integers in the sliding window.

# Implement the MovingAverage class:
# - MovingAverage(int size) Initializes the object with the size of the window
#   size.
# - double next(int val) Returns the moving average of the last size values of
#   the stream.
#
# Example 1:
# Input
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]
# Output
# [null, 1.0, 5.5, 4.66667, 6.0]

# Explanation
# MovingAverage movingAverage = new MovingAverage(3);
# movingAverage.next(1); // return 1.0 = 1 / 1
# movingAverage.next(10); // return 5.5 = (1 + 10) / 2
# movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
 
# Constraints:
# 1 <= size <= 1000
# -105 <= val <= 105
# At most 104 calls will be made to next.

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

################################################################################

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
        
        return sum(self.queue[-self.size:]) / min(len(self.queue), self.size)


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

#movingAverage = MovingAverage(3)
#print(movingAverage.next(1))		# 1.0 = 1 / 1
#print(movingAverage.next(10))		# 5.5 = (1 + 10) / 2
#print(movingAverage.next(3))		# 4.66667 = (1 + 10 + 3) / 3
#print(movingAverage.next(5))		# 6.0 = (10 + 3 + 5) / 3

movingAverage = MovingAverage(5)
print(movingAverage.next(12009))    # 12009.00000
print(movingAverage.next(1965))     # 6987.00000
print(movingAverage.next(-940))     # 4344.66667
print(movingAverage.next(-8516))    # 1129.50000
print(movingAverage.next(-16446))   # -2385.60000
print(movingAverage.next(7870))    # -3213.40000
print(movingAverage.next(25545))   # 1502.60000
print(movingAverage.next(-21028))  # -2515.00000
print(movingAverage.next(18430))   # 2874.20000
print(movingAverage.next(-2364))   # 5690.60000

## LeetCode Solutions
#########################

## Approach 1: Array or List
################################
# Time: O(N) - Where N is the size of the moving window, since we need to
#              retrieve N elements from the queue at each invocation of
#               next(val) function.
# Space: O(M) - Where M is the length of the queue which would grow at each
#               invocation of the next(val) function.
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        # calculate the sum of the moving window
        window_sum = sum(queue[-size:])

        return window_sum / min(len(queue), size)


## Approach 2: Double-ended Queue
#####################################
# Time: O(1) - As we explained in intuition.
# Space: O(N) - Where N is the size of the moving window.
from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        # number of elements seen so far
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0

        self.window_sum = self.window_sum - tail + val

        return self.window_sum / min(self.size, self.count)


## Approach 3: Circular Queue with Array
############################################
# Time: O(1) - As we can see that there is no loop in the next(val) function.
# Space: O(N) - Where N is the size of the circular queue.
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * self.size
        self.head = self.window_sum = 0
        # number of elements seen so far
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        # move on to the next head
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)


