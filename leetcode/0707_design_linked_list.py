"""
707. Design Linked List (medium)
"""


class SinglyLinkedNode:
    def __init__(self, val: int, next: "SinglyLinkedNode" = None) -> None:
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = SinglyLinkedNode(None, None)
        self.size = 0

    def get(self, index: int) -> int:
        if not (0 <= index < self.size):
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
        if index > self.size:
            return
        prev = self.head
        for _ in range(index):
            prev = prev.next
        node = SinglyLinkedNode(val)
        node.next, prev.next = prev.next, node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if not (0 <= index < self.size):
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        curr.next = curr.next.next
        self.size -= 1


class DoublyLinkedNode:
    def __init__(
        self,
        val: int,
        next: "DoublyLinkedNode" = None,
        prev: "DoublyLinkedNode" = None,
    ) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = DoublyLinkedNode(None)
        self.tail = DoublyLinkedNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _get_node(self, index: int) -> DoublyLinkedNode:
        if index + 1 < self.size - index:
            node = self.head
            for _ in range(index + 1):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.size - index):
                node = node.prev
        return node

    def get(self, index: int) -> int:
        if not (0 <= index < self.size):
            return -1
        curr = self._get_node(index)
        return curr.val

    def addAtHead(self, val: int) -> None:
        node = DoublyLinkedNode(val, self.head.next, self.head)
        self.head.next = node
        node.next.prev = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = DoublyLinkedNode(val, self.tail, self.tail.prev)
        self.tail.prev = node
        node.prev.next = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        curr = self._get_node(index)
        node = DoublyLinkedNode(val, curr, curr.prev)
        curr.prev = node
        node.prev.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if not (0 <= index < self.size):
            return
        curr = self._get_node(index)
        curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


def test1() -> None:
    ll = SinglyLinkedList()

    ll.addAtHead(1)
    print(ll.get(0))

    ll.addAtTail(3)
    print(ll.get(1))

    # linked list becomes: 1 -> 2 -> 3
    ll.addAtIndex(1, 2)
    print(ll.get(0), ll.get(1), ll.get(2))  # 1 2 3

    get1 = ll.get(1)
    print(get1)  # 2

    # linked list becomes: 1 -> 3
    ll.deleteAtIndex(1)
    print(ll.get(0), ll.get(1))  # 1 3

    get2 = ll.get(1)
    print(get2)  # 3


def print_ll(ll: DoublyLinkedList) -> None:
    curr = ll.head
    vals = []
    while curr:
        vals.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(vals))


def test2() -> None:
    ll = DoublyLinkedList()

    ll.addAtHead(2)
    print_ll(ll)  # None -> 2 -> None

    ll.deleteAtIndex(1)
    print_ll(ll)  # None -> 2 -> None

    ll.addAtHead(2)
    print_ll(ll)  # None -> 2 -> 2 -> None

    ll.addAtHead(7)
    print_ll(ll)  # None -> 7 -> 2 -> 2 -> None

    ll.addAtHead(3)
    print_ll(ll)  # None -> 3 -> 7 -> 2 -> 2 -> None

    ll.addAtHead(2)
    print_ll(ll)  # None -> 2 -> 3 -> 7 -> 2 -> 2 -> None

    ll.addAtHead(5)
    print_ll(ll)  # None -> 5 -> 2 -> 3 -> 7 -> 2 -> 2 -> None

    ll.addAtTail(5)
    print_ll(ll)  # None -> 5 -> 2 -> 3 -> 7 -> 2 -> 2 -> 5 -> None

    get1 = ll.get(5)
    print(get1)  # 2

    ll.deleteAtIndex(6)
    print_ll(ll)  # None -> 5 -> 2 -> 3 -> 7 -> 2 -> 2 -> None

    ll.deleteAtIndex(4)
    print_ll(ll)  # None -> 5 -> 2 -> 3 -> 7 -> 2 -> None


test1()
print("-" * 88)
test2()
