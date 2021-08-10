##
#### Design Circular Queue (medium)
#######################################

# Design your implementation of the circular queue. The circular queue is a
# linear data structure in which the operations are performed based on FIFO
# (First In First Out) principle and the last position is connected back to the
# first position to make a circle. It is also called "Ring Buffer".

# One of the benefits of the circular queue is that we can make use of the
# spaces in front of the queue. In a normal queue, once the queue becomes full,
# we cannot insert the next element even if there is a space in front of the
# queue. But using the circular queue, we can use the space to store new values.

# Implementation the MyCircularQueue class:
# - MyCircularQueue(k) Initializes the object with the size of the queue
#   to be k.
# - int Front() Gets the front item from the queue. If the queue is empty,
#   return -1.
# - int Rear() Gets the last item from the queue. If the queue is empty,
#   return -1.
# - boolean enQueue(int value) Inserts an element into the circular queue.
#   Return true if the operation is successful.
# - boolean deQueue() Deletes an element from the circular queue. Return true
#   if the operation is successful.
# - boolean isEmpty() Checks whether the circular queue is empty or not.
# - boolean isFull() Checks whether the circular queue is full or not.

# You must solve the problem without using the built-in queue data structure in
# your programming language. 

# Example 1:

# Input
# ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear",
# "isFull", "deQueue", "enQueue", "Rear"]
# [[3], [1], [2], [3], [4], [], [], [], [4], []]

# Output
# [null, true, true, true, false, 3, true, true, true, 4]

# Explanation
# MyCircularQueue myCircularQueue = new MyCircularQueue(3);
# myCircularQueue.enQueue(1); // return True
# myCircularQueue.enQueue(2); // return True
# myCircularQueue.enQueue(3); // return True
# myCircularQueue.enQueue(4); // return False
# myCircularQueue.Rear();     // return 3
# myCircularQueue.isFull();   // return True
# myCircularQueue.deQueue();  // return True
# myCircularQueue.enQueue(4); // return True
# myCircularQueue.Rear();     // return 4
 
# Constraints:
# 1 <= k <= 1000
# 0 <= value <= 1000
# At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty,
# and isFull.

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

################################################################################

## attempt 1
################
class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.queue[self.rear] = value
        self.rear += 1
        if self.rear >= len(self.queue):
            self.rear = 0
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.queue[self.front] = None
        self.front += 1
        if self.front >= len(self.queue):
            self.front = 0
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.rear - 1]

    def isEmpty(self) -> bool:
        return all(x == None for x in self.queue)

    def isFull(self) -> bool:
        return not(None in self.queue)


## array
############
class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.capacity = k
        self.head = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        tail = (self.head + self.size) % self.capacity
        self.queue[tail] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        tail = (self.head + self.size - 1) % self.capacity
        return self.queue[tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacityclass


## array thread safe
########################
from threading import Lock

class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [0]*k
        self.headIndex = 0
        self.count = 0
        self.capacity = k
        self.queueLock = Lock()
        
    def enQueue(self, value: int) -> bool:
        with self.queueLock:
            if self.count == self.capacity:
                return False
            self.queue[(self.headIndex + self.count) % self.capacity] = value
            self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.headIndex = (self.headIndex + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.headIndex]

    def Rear(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[(self.headIndex + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity
        

## linked list
##################
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        

class MyCircularQueue:
    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.capacity = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        new = ListNode(value)
        if self.isEmpty():
            self.head = new
            self.tail = self.head
        else:
            self.tail.next = new
            self.tail = new
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.head = self.head.next
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.head.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


class MyCircularQueue:
    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.capacity = k
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        
        if self.size == 0:
            self.head = ListNode(value)
            self.tail = self.head
        else:
            self.tail.next = ListNode(value)
            self.tail = self.tail.next
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.head = self.head.next
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.head.value

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.tail.value
    
    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


## Tests
#############

#myCircularQueue = MyCircularQueue(3)
#print(myCircularQueue.enQueue(1))   # return True
#print(myCircularQueue.enQueue(2))   # return True
#print(myCircularQueue.enQueue(3))   # return True
#print(myCircularQueue.enQueue(4))   # return False
#print(myCircularQueue.Rear())      # return 3
#print(myCircularQueue.isFull())    # return True
#print(myCircularQueue.deQueue())   # return True
#print(myCircularQueue.enQueue(4))  # return True
#print(myCircularQueue.Rear())      # return 4
#print('---------------------------------')
#print('is empty:', myCircularQueue.isEmpty())
#print('is full:', myCircularQueue.isFull())
#print('front:', myCircularQueue.front)
#print('rear:', myCircularQueue.rear)
#print(myCircularQueue.queue)

#myCircularQueue = MyCircularQueue(3)
#print(myCircularQueue.enQueue(1))   # True
#print(myCircularQueue.enQueue(2))   # True
#print(myCircularQueue.enQueue(3))   # True
#print(myCircularQueue.enQueue(4))   # False
#print(myCircularQueue.Rear())       # 3
#print(myCircularQueue.isFull())     # True
#print(myCircularQueue.deQueue())    # True
#print(myCircularQueue.enQueue(4))   # True
#print(myCircularQueue.Rear())       # 4


def print_LL(root):
    if not root:
        return print('invalid root')
    
    result = []
    while root:
        result.append(root.val)
        root = root.next

    print(result)

#print_LL(myCircularQueue.head)


## LeetCode Solutions
#########################

## Approach 1: Array
########################
# Time: O(1) - All of the methods in our circular data structure is of constant
#              time complexity.
# Space: O(N)
# The overall space complexity of the data structure is linear, where N is the
# pre-assigned capacity of the queue. However, it is worth mentioning that the
# memory consumption of the data structure remains as its pre-assigned capacity
# during its entire life cycle.
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [0]*k
        self.headIndex = 0
        self.count = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.count == self.capacity:
            return False
        self.queue[(self.headIndex + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        self.headIndex = (self.headIndex + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.count == 0:
            return -1
        return self.queue[self.headIndex]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        # empty queue
        if self.count == 0:
            return -1
        return self.queue[(self.headIndex + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.capacity


## Approach 1: Array - Improvement: Thread-Safe
###################################################
# This time, it is not about the space or time complexity, but concurrency. Our
# circular queue is NOT thread-safe. One could end up with corrupting our data
# structure in a multi-threaded environment.

# There are several ways to mitigate the above concurrency problem. Take the
# function enQueue(int value) as an example, we show how we can make the
# function thread-safe in the following implementation:
from threading import Lock

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [0]*k
        self.headIndex = 0
        self.count = 0
        self.capacity = k
        # the additional attribute to protect the access of our queue
        self.queueLock = Lock()

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        # automatically acquire the lock when entering the block
        with self.queueLock:
            if self.count == self.capacity:
                return False
            self.queue[(self.headIndex + self.count) % self.capacity] = value
            self.count += 1
        # automatically release the lock when leaving the block
        return True


## Approach 2: Singly-Linked List
#####################################
# Time: O(1) - For each method in our circular queue.
# Space: O(N) - The upper bound of the memory consumption for our circular queue#               would be O(N), same as the Array approach. However, it should be#               more memory efficient as we discussed in the intuition section.
class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.capacity = k
        self.head = None
        self.tail = None
        self.count = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.count == self.capacity:
            return False
        
        if self.count == 0:
            self.head = Node(value)
            self.tail = self.head
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1
        return True


    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -= 1
        return True


    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.count == 0:
            return -1
        return self.head.value

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        # empty queue
        if self.count == 0:
            return -1
        return self.tail.value
    
    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.capacity


################################################################################


class MyCircularQueue:
    def __init__(self, k: int):
        pass

    def enQueue(self, value: int) -> bool:
        pass

    def deQueue(self) -> bool:
        pass

    def Front(self) -> int:
        pass

    def Rear(self) -> int:
        pass

    def isEmpty(self) -> bool:
        pass

    def isFull(self) -> bool:
        pass

