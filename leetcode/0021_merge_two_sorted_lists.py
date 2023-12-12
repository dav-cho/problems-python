"""
21. Merge Two Sorted Lists (easy)
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Recursive:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        list2.next = self.mergeTwoLists(list1, list2.next)
        return list2


class Iterative:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sentinel = ListNode(None)
        curr = sentinel
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 if list1 else list2
        return sentinel.next


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
