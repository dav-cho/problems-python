##
#### 622. Design Circular Queue (medium)
############################################


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
        return not (None in self.queue)


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
        self.queue = [0] * k
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

# myCircularQueue = MyCircularQueue(3)
# print(myCircularQueue.enQueue(1))   # return True
# print(myCircularQueue.enQueue(2))   # return True
# print(myCircularQueue.enQueue(3))   # return True
# print(myCircularQueue.enQueue(4))   # return False
# print(myCircularQueue.Rear())      # return 3
# print(myCircularQueue.isFull())    # return True
# print(myCircularQueue.deQueue())   # return True
# print(myCircularQueue.enQueue(4))  # return True
# print(myCircularQueue.Rear())      # return 4
# print('---------------------------------')
# print('is empty:', myCircularQueue.isEmpty())
# print('is full:', myCircularQueue.isFull())
# print('front:', myCircularQueue.front)
# print('rear:', myCircularQueue.rear)
# print(myCircularQueue.queue)

# myCircularQueue = MyCircularQueue(3)
# print(myCircularQueue.enQueue(1))   # True
# print(myCircularQueue.enQueue(2))   # True
# print(myCircularQueue.enQueue(3))   # True
# print(myCircularQueue.enQueue(4))   # False
# print(myCircularQueue.Rear())       # 3
# print(myCircularQueue.isFull())     # True
# print(myCircularQueue.deQueue())    # True
# print(myCircularQueue.enQueue(4))   # True
# print(myCircularQueue.Rear())       # 4


def print_LL(root):
    if not root:
        return print("invalid root")

    result = []
    while root:
        result.append(root.val)
        root = root.next

    print(result)


# print_LL(myCircularQueue.head)
