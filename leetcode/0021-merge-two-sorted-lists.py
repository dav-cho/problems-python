##
#### 21. Merge Two Sorted Lists (easy)
##########################################


from typing import Optional


## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## iterative
##############################
class Solution:
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sentinel = ListNode(None)
        curr = sentinel

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        curr.next = l1 if l1 else l2

        return sentinel.next


## recursive
##############################
class Solution:
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1

        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


## first attempt
##############################
class Solution:
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sentinel = ListNode(None)
        curr = sentinel

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        curr.next = l1 if l1 else l2

        return sentinel.next


## Tests
############

test1 = ([1, 2, 4], [1, 3, 4])  # [1, 1, 2, 3, 4, 4]
test2 = ([], [])  # []
test3 = ([], [0])  # [0]


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
                head1 = ListNode(test[0][0])
            if not test[1]:
                head2 = []
            else:
                head2 = ListNode(test[1][0])

            current1 = head1
            for i in range(1, len(test[0])):
                current1.next = ListNode(test[0][i])
                current1 = current1.next
            current2 = head2
            for i in range(1, len(test[1])):
                current2.next = ListNode(test[1][i])
                current2 = current2.next

            print_LL(head1, "l1:")
            print_LL(head2, "l2:")
            solution = Solution()
            result = solution.mergeTwoLists(head1, head2)
            print_LL(result, "result:")

    return run()


def print_LL(head, msg="print_LL"):
    linked_list = []

    while head:
        linked_list.append(head.val)
        head = head.next

    print(msg, linked_list)


test(test1, test2, test3)
