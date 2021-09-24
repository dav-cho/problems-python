##
#### Linked List Cycle (easy)
########################################

# Given head, the head of a linked list, determine if the linked list has a
# cycle in it.

# There is a cycle in a linked list if there is some node in the list that can
# be reached again by continuously following the next pointer. Internally, pos
# is used to denote the index of the node that tail's next pointer is connected
# to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
 
# Constraints:
# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.
 
# Follow up: Can you solve it using O(1) (i.e. constant) memory?

################################################################################

## Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


## two-pointer (floyd's algorithm)
######################################
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            
            if head == fast:
                return True
            
        return False


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            if not fast or not fast.next:
                return False
            
            slow = slow.next
            fast = fast.next.next
            
        return True


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        
        fast = head.next
        
        while fast and fast.next:
            if head == fast:
                return True
            
            head = head.next
            fast = fast.next.next
            
        return False


## hash table
##############################
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        
        while head:
            if head in seen:
                return True
            
            seen.add(head)
            head = head.next
            
        return False


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = {head}
        
        while head:
            head = head.next
            
            if head in seen:
                return True
            
            seen.add(head)
            
        return False


## first attempt
##############################
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            
            if head == fast:
                return True
            
        return False


## 
##############################
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        pass


## 
##############################
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Hash Table
##############################
# Time: O(n) - We visit each of the nn elements in the list at most once. Adding
#              a node to the hash table costs only O(1) time.
# Space: O(n) - The space depends on the number of elements added to the hash
#               table, which contains at most n elements.
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False


## Approach 2: Floyd's Cycle Finding Algorithm
##################################################
# Time: 
# Space: 
# Time: O(n) - Let us denote nn as the total number of nodes in the linked list.
#              To analyze its time complexity, we consider the following two
#              cases separately.
# - List has no cycle:
#   - The fast pointer reaches the end first and the run time depends on the
#     list's length, which is O(n).
# - List has a cycle:
#   - We break down the movement of the slow pointer into two steps, the
#     non-cyclic part and the cyclic part:
#       1. The slow pointer takes "non-cyclic length" steps to enter the cycle.
#          At this point, the fast pointer has already reached the cycle.
#          Number of iterations = non-cyclic length = N
#       2. Both pointers are now in the cycle. Consider two runners running in a
#          cycle - the fast runner moves 2 steps while the slow runner moves 1
#          steps at a time. Since the speed difference is 1, it takes
#          (distance between the 2 runners) / (difference of speed) loops for
#          the fast runner to catch up with the slow runner. As the distance is
#          at most "cyclic length K" and the speed difference is 1, we conclude
#          that Number of iterations = almost "cyclic length K".
# - Therefore, the worst case time complexity is O(N+K), which is O(n).

# Space: O(1)
# - We only use two nodes (slow and fast) so the space complexity is O(1).

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


