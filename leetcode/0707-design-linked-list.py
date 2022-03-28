##
#### 707. Design Linked List (medium)
#########################################


## singly linked list
#########################
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = ListNode(None)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head
        for _ in range(index + 1):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next

        new = ListNode(val)
        new.next = prev.next
        prev.next = new
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next

        prev.next = prev.next.next
        self.size -= 1


## doubly linked list
#########################
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:
    def __init__(self):
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.size = 0

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev

        return curr.val

    def addAtHead(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.head.next
        new.prev = self.head
        self.head.next.prev = new
        self.head.next = new
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.tail
        new.prev = self.tail.prev
        self.tail.prev.next = new
        self.tail.prev = new
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index < self.size - index:
            prev = self.head
            for _ in range(index):
                prev = prev.next
            next = prev.next
        else:
            next = self.tail
            for _ in range(self.size - index):
                next = next.prev
            prev = next.prev

        new = ListNode(val)
        new.next = next
        new.prev = prev
        prev.next = new
        next.prev = new
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index < self.size - index:
            prev = self.head
            for _ in range(index):
                prev = prev.next
            next = prev.next.next
        else:
            next = self.tail
            for _ in range(self.size - index - 1):
                next = next.prev
            prev = next.prev.prev

        prev.next = next
        next.prev = prev
        self.size -= 1


## Tests
############

test1 = MyLinkedList()
test1.addAtHead(1)
print(test1.get(0))
test1.addAtTail(3)
print(test1.get(1))
test1.addAtIndex(1, 2)  # linked list becomes 1 -> 2 -> 3
print(test1.get(0), test1.get(1), test1.get(2))
print(test1.get(1))  # return 2
test1.deleteAtIndex(1)
# now the linked list is 1 -> 3
print(test1.get(0), test1.get(1))
print(test1.get(1))  # return 3
