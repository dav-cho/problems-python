##
#### 138. Copy List with Random Pointer (medium)
####################################################


## Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


## recursive
################
class Solution:
    def __init__(self):
        self.visited = {}

    def copy_random_list(self, head: Node) -> Node:
        if not head:
            return

        if head in self.visited:
            return self.visited[head]

        new = Node(head.val)
        self.visited[head] = new

        new.next = self.copy_random_list(head.next)
        new.random = self.copy_random_list(head.random)

        return new


## iterative
################
class Solution:
    def __init__(self):
        self.visited = {}

    def get_clone(self, node):
        if not node:
            return
        if node not in self.visited:
            self.visited[node] = Node(node.val)

        return self.visited[node]

    def copy_random_list(self, head: Node) -> Node:
        if not head:
            return

        old = head
        new = Node(old.val)
        self.visited[old] = new

        while old:
            new.next = self.get_clone(old.next)
            new.random = self.get_clone(old.random)

            old = old.next
            new = new.next

        return self.visited[head]


## iterative with O(1) space
################################
class Solution:
    def copy_random_list(self, head: Node) -> Node:
        if not head:
            return

        curr = head
        while curr:
            new = Node(curr.val)
            new.next = curr.next
            curr.next = new
            curr = new.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        old_curr = head
        new_curr = new_head = head.next
        while old_curr:
            old_curr.next = old_curr.next.next
            if new_curr.next:
                new_curr.next = new_curr.next.next
            old_curr = old_curr.next
            new_curr = new_curr.next

        return new_head


## Tests
############

test1 = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
# [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]

test2 = [[1, 1], [2, 1]]
# [[1, 1], [2, 1]]

test3 = [[3, None], [3, 0], [3, None]]
# [[3,None],[3,0],[3,None]]

test4 = []
# []

tests = (
    test1,
    test2,
    test3,
    test4,
)


def test(*args):
    count = 1

    def run():
        for test in args:
            nonlocal count
            print(f"~ test{count}")
            count += 1

            if not test:
                head = []
            else:
                seen = []
                prev = head = None

                for i in range(len(test)):
                    new = Node(test[i][0])
                    seen.append(new)

                    if not head:
                        head = new
                    if prev:
                        prev.next = new
                    prev = new

                curr = head
                for i in range(len(test)):
                    if test[i][1] is not None:
                        curr.random = seen[test[i][1]]
                    curr = curr.next

            print_LL(head, "list")

            solution = Solution()
            result = solution.copy_random_list(head)

            print_LL(result, "result")

    return run()


def print_LL(head, msg="print_LL"):
    arr, seen = [], set()

    temp = [None, None]
    while head:
        if head in seen:
            break

        temp[0] = head.val
        temp[1] = head.random.val if head.random else None
        arr.append(temp)
        seen.add(head)
        temp = [None, None]
        head = head.next

    print(msg, arr)


test(*tests)
