##
#### 2. Add Two Numbers (medium)
###################################


## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## simple math
##################
class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = curr = ListNode(None)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            carry, val = divmod(carry, 10)
            curr.next = ListNode(val)
            curr = curr.next

        return sentinel.next


class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = curr = ListNode(None)
        carry = 0
        while l1 or l2 or carry:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            curr.next = ListNode(val)
            curr = curr.next

        return sentinel.next


class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = curr = ListNode(None)
        carry = 0
        while l1 or l2 or carry:
            x = y = 0
            if l1:
                x = l1.val
                l1 = l1.next
            if l2:
                y = l2.val
                l2 = l2.next

            carry, val = divmod(x + y + carry, 10)
            curr.next = ListNode(val)
            curr = curr.next

        return sentinel.next


## convert to string
########################
class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        while l1:
            num1 += str(l1.val)
            l1 = l1.next

        num2 = ""
        while l2:
            num2 += str(l2.val)
            l2 = l2.next

        sum = [int(x) for x in (str(int(num1[::-1]) + int(num2[::-1])))][::-1]
        head = curr = ListNode(sum[0])

        for i in range(1, len(sum)):
            curr.next = ListNode(sum[i])
            curr = curr.next

        return head


## Tests
############

test1 = ([2, 4, 3], [5, 6, 4])  # [7, 0, 8]
test2 = ([0], [0])  # [0]
test3 = ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9])  # [8, 9, 9, 9, 0, 0, 0, 1]


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
            result = solution.add_two_numbers(head1, head2)
            print_LL(result, "result:")

    return run()


def print_LL(head, msg="print_LL"):
    linked_list = []

    while head:
        linked_list.append(head.val)
        head = head.next

    print(msg, linked_list)


test(test1, test2, test3)
