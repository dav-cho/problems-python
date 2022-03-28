##
#### 708. Insert into a Sorted Circular Linked List (medium)
################################################################


## Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


## TODO: find min and max
#######################
class Solution:
    def insert(self, head: Node, insertVal: int) -> Node:
        new = Node(insertVal)

        if not head:
            new.next = new
            return new
        if head == head.next:
            head.next, new.next = new, head
            return head

        mn = mx = head.val
        curr = head.next
        while True:
            if curr == head:
                break
            mn = min(mn, curr.val)
            mx = max(mx, curr.val)
            curr = curr.next

        prev = head

        new.next, prev.next = prev.next, new

        return head


## two pointer iteration 1
##############################
class Solution:
    def insert(self, head: Node, insertVal: int) -> Node:
        new = Node(insertVal)

        if not head:
            new.next = new
            return new

        prev = head
        while True:
            if prev.val <= insertVal <= prev.next.val:
                break
            if prev.val > prev.next.val:
                if insertVal >= prev.val or insertVal <= prev.next.val:
                    break
            if prev.next == head:
                break
            prev = prev.next

        new.next, prev.next = prev.next, new

        return head


## two pointer iteration 2
##############################
class Solution:
    def insert(self, head: Node, insertVal: int) -> Node:
        new = Node(insertVal)

        if not head:
            new.next = new
            return new

        prev = head
        while True:
            if prev.val <= insertVal <= prev.next.val:
                break
            if prev.val > prev.next.val:
                if insertVal >= prev.val or insertVal <= prev.next.val:
                    break

            prev = prev.next
            if prev == head:
                break

        new.next, prev.next = prev.next, new

        return head


## Tests
############

test1 = ([3, 4, 1], 2)  # [3, 4, 1, 2]
test2 = ([], 1)  # [1]
test3 = ([1], 0)  # [1, 0]
test4 = ([3, 3, 3], 0)  # [3, 3, 3, 0]
test5 = ([1, 3, 5], 4)  # [1, 3, 4, 5]
test6 = ([3, 5, 1], 0)  # [3, 5, 0, 1]

tests = (
    test1,
    test2,
    test3,
    test4,
    test5,
    test6,
    ([3, 5, 1], 0),
    ([3, 5, 1], 6),
    ([3, 3, 3], 0),
    ([3, 3, 3], 6),
    ([3, 4, 1], 2),
)


def test(*args):
    count = 1

    def run():
        for test in args:
            nonlocal count
            print(f"~ test{count}")
            count += 1

            linked_list, val = test

            if not linked_list:
                head = []
            else:
                head = Node(linked_list[0])
                curr = head
                for i in range(1, len(linked_list)):
                    curr.next = Node(linked_list[i])
                    curr = curr.next

                curr.next = head

            print("insert", val)
            print_LL(head, "list")

            solution = Solution()
            result = solution.insert(head, val)

            print_LL(result, "result")

    return run()


def print_LL(head, msg="print_LL"):
    arr, seen = [], set()

    while head:
        if head in seen:
            break
        arr.append(head.val)
        seen.add(head)
        head = head.next

    print(msg, arr)


test(*tests)
