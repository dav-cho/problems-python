##
#### Rotate List (medium)
#############################

# Given the head of a linked list, rotate the list to the right by k places.

# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]

# Example 2:
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
 
# Constraints:
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 109

################################################################################

## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## attempt 1
################
# find k'th value from end and connect to head, return k'th node
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return

        curr = head
        size = 0
        while curr:
            curr = curr.next
            size += 1

        if k > size:
            k = k % size

        left = right = head
        for _ in range(k):
            right = right.next
        while right.next:
            right = right.next
            left = left.next
        right.next = head
        left.next, left = None, left.next

        return left


## approach 1
#################
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        if not head.next:
            return head
        
        old_tail, size = head, 1
        while old_tail.next:
            old_tail = old_tail.next
            size += 1
        old_tail.next = head    
        
        k = k % size
        new_tail = head
        for _ in range(size - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next    
        new_tail.next = None
        
        return new_head


## Tests
############

test1 = ([1, 2, 3, 4, 5], 2)    # [4, 5, 1, 2, 3]
test2 = ([0, 1, 2], 4)          # [2, 0, 1]
test3 = ([1], 1)                # [1]
test4 = ([1, 2], 2)             # [1, 2]

tests = (
    test1,
    test2,
    test3,
    test4
)


def test(*args):
    count = 1

    def run():
        for test in args:
            nonlocal count
            print(f"~ test{count}")
            count += 1

            arr, k = test
            
            if not arr:
                head = []
            else:
                head = ListNode(arr[0])

                curr = head
                for i in range(1, len(arr)):
                    curr.next = ListNode(arr[i])
                    curr = curr.next

            print_LL(head, "original:")
            print("k:", k)

            solution = Solution()
            result = solution.rotateRight(head, k)

            print_LL(result, "result:")

    return run()


def print_LL(head, msg="print_LL"):
    vals = []

    while head:
        vals.append(head.val)
        head = head.next

    print(msg, vals)


test(*tests)

## LeetCode Solutions
#########################

## Approach 1: 
#################
# time: O(n) - where n is number of elements in the list.
# space: O(1) - since it's a constant space solution.
class Solution:
    def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
        # base cases
        if not head:
            return None
        if not head.next:
            return head
        
        # close the linked list into the ring
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head
        
        # find new tail : (n - k % n - 1)th node
        # and new head : (n - k % n)th node
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # break the ring
        new_tail.next = None
        
        return new_head

