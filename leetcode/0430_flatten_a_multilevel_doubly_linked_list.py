##
#### 430. Flatten a Multilevel Doubly Linked List (medium)
##############################################################


## Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


## simple
#############
class Solution:
    def flatten(self, head: "Node") -> "Node":
        if not head:
            return

        curr = head
        while curr:
            if not curr.child:
                curr = curr.next
                continue

            child_tail = curr.child
            while child_tail.next:
                child_tail = child_tail.next

            if curr.next:
                curr.next.prev = child_tail
            child_tail.next = curr.next
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None

        return head


## stack
############
class Solution:
    def flatten(self, head: "Node") -> "Node":
        if not head:
            return

        sentinel = Node(None, None, head, None)
        stack = [head]
        prev = sentinel
        while stack:
            curr = stack.pop()
            curr.prev = prev
            prev.next = curr

            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
            prev = curr

        sentinel.next.prev = None
        return sentinel.next


### dfs recursive
#####################
class Solution:
    def flatten(self, head: "Node") -> "Node":
        if not head:
            return

        sentinel = Node(None, None, head, None)
        self.flatten_dfs(sentinel, head)
        sentinel.next.prev = None

        return sentinel

    def flatten_dfs(self, prev, curr):
        if not curr:
            return prev

        curr.prev, prev.next = prev, curr
        temp_next = curr.next
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None

        return self.flatten_dfs(tail, temp_next)


## dfs iterative
####################
class Solution:
    def flatten(self, head: "Node") -> "Node":
        if not head:
            return

        sentinel = Node(None, None, head, None)
        prev = sentinel

        stack = [head]
        while stack:
            curr = stack.pop()
            prev.next, curr.prev = curr, prev

            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None

            prev = curr

        sentinel.next.prev = None

        return sentinel.next


## Tests
############


def test1():
    pass


def test(*args):
    count = 1

    def run():
        for test in args:
            nonlocal count
            print(f"~ test{count}")
            count += 1

            if not test[0]:
                head1 = []
            else:
                head1 = Node(test[0][0])
            if not test[1]:
                head2 = []
            else:
                head2 = Node(test[1][0])

            current1 = head1
            for i in range(1, len(test[0])):
                current1.next = Node(test[0][i])
                current1 = current1.next
            current2 = head2
            for i in range(1, len(test[1])):
                current2.next = Node(test[1][i])
                current2 = current2.next

            print_LL(head1, "l1:")
            print_LL(head2, "l2:")
            solution = Solution()
            result = solution.add_two_numbers(head1, head2)
            print_LL(result, "result:")

    return run()


def print_LL(head, msg="print_LL"):
    linked_list = []

    while head:
        linked_list.append(head.val)
        head = head.next

    print(msg, linked_list)
