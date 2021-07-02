##
#### Reverse Linked List (easy)
###################################

# Given the head of a singly linked list,
# reverse the list, and return the reversed list.

# Example 1:
# 1 -> 2 -> 3 -> 4 -> 5
# 5 -> 4 -> 3 -> 2 -> 1
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# 1 -> 2
# 2 -> 1
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

# Constraints:
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000

# Follow up: A linked list can be reversed either
# iteratively or recursively. Could you implement both?

######################################################################


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


# Approach 1: Iterative
def reverseList(head: ListNode) -> ListNode:
    prev = None
    current = head

    while current:
        # next = current.next
        # current.next = prev
        # prev = current
        # current = next
        current.next, prev, current = prev, current, current.next

    return prev


# Approach 2: Recursive
def reverseList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    p = reverseList(head.next)
    head.next.next = head
    head.next = None

    return p


def test(*args):
    count = 1

    def run():
        for test in args:
            if not test:
                return []

            head = ListNode(test[0])
            current = head

            for i in range(1, len(test)):
                current.next = ListNode(test[i])
                current = current.next

            result = reverseList(head)
            nonlocal count
            print(f"test: {count}")
            print(f"result {count}: {result}")
            count += 1

    return run()


test1 = [1, 2, 3, 4, 5]
test2 = [1, 2]
test3 = []

test(test1, test2, test3)
