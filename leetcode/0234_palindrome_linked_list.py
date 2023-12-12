##
#### 234. Palindrome Linked List (easy)
###########################################


## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## extra array
##############################
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []

        while head:
            vals.append(head.val)
            head = head.next

        return vals == vals[::-1]


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []

        while head:
            vals.append(head.val)
            head = head.next

        N = len(vals)

        for i in range(N // 2):
            if vals[i] != vals[~i + N]:
                return False

        return True


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []

        while head:
            vals.append(head.val)
            head = head.next

        left, right = 0, len(vals) - 1

        while left < right:
            if vals[left] != vals[right]:
                return False

            left += 1
            right -= 1

        return True


## recursive
##############################
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def helper(node):
            nonlocal head

            if not node:
                return True
            if not helper(node.next) or node.val != head.val:
                return False

            head = head.next

            return True

        return helper(head)


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def helper(node):
            nonlocal head

            if node:
                if not helper(node.next) or node.val != head.val:
                    return False

                head = head.next

            return True

        return helper(head)


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        curr = head

        def helper(node):
            nonlocal head

            if node:
                if not helper(node.next) or node.val != head.val:
                    return False

                head = head.next

            return True

        return helper(curr)


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def helper(node):
            nonlocal head

            if not node:
                return True

            if not helper(node.next) or node.val != head.val:
                return False

            head = head.next

            return True

        return helper(head)


## reverse second half
##############################
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow = slow.next
        prev = None

        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        while prev:
            if head.val != prev.val:
                return False

            head = head.next
            prev = prev.next

        return True


## Tests
#############


test1 = [1, 2, 2, 1]  # True
test2 = [1, 2]  # False


def test(*args):
    count = 1

    def run():
        for test in args:
            nonlocal count
            print("~ test", count)
            count += 1

            if not test:
                print("[]")
                continue

            head = ListNode(test[0])
            current = head

            for i in range(1, len(test)):
                current.next = ListNode(test[i])
                current = current.next

            print_LL(head)
            solution = Solution()
            result = solution.isPalindrome(head)
            print(result)

    return run()


def print_LL(head):
    linked_list = []

    while head:
        linked_list.append(head.val)
        head = head.next

    print(linked_list)


test(test1, test2)
