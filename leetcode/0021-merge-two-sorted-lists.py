##
#### Merge Two Sorted Lists (easy)
######################################

# Merge two sorted linked lists and return it as a sorted list. The list
# should be made by splicing together the nodes of the first two lists.

# Example 1:
# [1] -> [2] -> [3] 
# (1) -> (3) -> (4)
# (1) -> [1] -> [2] -> (3) -> [4] -> (4)
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: l1 = [], l2 = []
# Output: []

# Example 3:
# Input: l1 = [], l2 = [0]
# Output: [0]
 
# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both l1 and l2 are sorted in non-decreasing order.

################################################################################

## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## first attempt
####################
class Solution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return
        if not l1:
            return l2
        if not l2:
            return l2

        head = ListNode(None)
        curr = head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 if l1 else l2

        return head.next


## recursive
################
class Solution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.merge_two_lists(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two_lists(l1, l2.next)
            return l2


## iterative
################
class Solution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = ListNode(None)

        curr = sentinel
        while l1 and l2:
            if l1.val <= l2.val:
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
test2 = ([], [])                # []
test3 = ([], [0])               # [0]

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

            print_LL(head1, 'l1:')
            print_LL(head2, 'l2:')
            solution = Solution()
            result = solution.merge_two_lists(head1, head2)
            print_LL(result, 'result:')

    return run()


def print_LL(head, msg="print_LL"):
    linked_list = []

    while head:
        linked_list.append(head.val)
        head = head.next

    print(msg, linked_list)


test(test1, test2, test3)
        

## LeetCode Solutions
#########################

## Approach 1: Recursion
############################
# time: O(n + m) - Because each recursive call increments the pointer to
#                  l1 or l2 by one (approaching the dangling null at the end
#                  of each list), there will be exactly one call to
#                  mergeTwoLists per element in each list. Therefore, the time
#                  complexity is linear in the combined size of the lists.

# space: O(n + m) - The first call to mergeTwoLists does not return until the
#                   ends of both l1 and l2 have been reached, so n + m stack
#                   frames consume O(n + m) space.

# Intuition:
# We can recursively define the result of a merge operation on two lists
# as the following (avoiding the corner case logic surrounding empty lists):

# list1[0] + merge(list1[1:], list2)    (list1[0] < list2[0])
# list2[0] + merge(list1, list2[1:])    (otherwise)

# Namely, the smaller of the two lists' heads plus the result of a
# merge on the rest of the elements.

# Algorithm:
# We model the above recurrence directly, first accounting for edge cases.
# Specifically, if either of l1 or l2 is initially null, there is no merge
# to perform, so we simply return the non-null list. Otherwise, we determine
# which of l1 and l2 has a smaller head, and recursively set the next value
# for that head to the next merge result. Given that both lists are
# null-terminated, the recursion will eventually terminate.

# Implementation:
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


## Approach 2: Iteration
############################
# time: O(n + m) - Because exactly one of l1 and l2 is incremented on each
#                  loop iteration, the while loop runs for a number of
#                  iterations equal to the sum of the lengths of the two lists.
#                  All other work is constant, so the overall complexity is
#                  linear.

# space: O(1) - The iterative approach only allocates a few pointers, so it
#               has a constant overall memory footprint.

# Intuition:
# We can achieve the same idea via iteration by assuming that l1 is entirely
# less than l2 and processing the elements one-by-one, inserting elements
# of l2 in the necessary places in l1.

# Algorithm:
# First, we set up a false "prehead" node that allows us to easily return the
# head of the merged list later. We also maintain a prev pointer, which points
# to the current node for which we are considering adjusting its next pointer.
# Then, we do the following until at least one of l1 and l2 points to null:
# if the value at l1 is less than or equal to the value at l2, then we connect
# l1 to the previous node and increment l1. Otherwise, we do the same, but for
# l2. Then, regardless of which list we connected, we increment prev to keep
# it one step behind one of our list heads.

# After the loop terminates, at most one of l1 and l2 is non-null. Therefore
# (because the input lists were in sorted order), if either list is non-null,
# it contains only elements greater than all of the previously-merged elements.
# This means that we can simply connect the non-null list to the merged list
# and return it.

# Implementation:
class Solution:
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next


