##
#### Linked List Cycle (easy)
#################################

# Given head, the head of a linked list, determine if the linked
# list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that
# can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's
# next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list,
# where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list,
# where the tail connects to the 0th node.

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


## hash table
#################
# time: O(n) - have to cycle at most n times
# space: O(n) - for the hash table
class Solution:
    def has_cycle(self, head: ListNode) -> bool:
        seen = set()

        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next

        return False

## 2 pointer floyd's cycle finding algorithm (hare and tortoise)
###################################################################
# time: 
# space: 
class Solution:
    def has_cycle(self, head: ListNode) -> bool:
        if not head:
            return False

        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next

        return True


## Tests
############


## LeetCode Solutions
#########################

## Approach 1: Hash Table
#############################
# time: O(n) - We visit each of the n elements in the list at most once.
#              Adding a node to the hash table costs only O(1) time.
# space: O(n) - The space depends on the number of elements added to the
#               hash table, which contains at most n elements.
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
# time: O(n) - Where n is total number of nodes in the linked list.

# To analyze its time complexity,
# we consider the following two cases separately.
#   List has no cycle:
#   - The fast pointer reaches the end first and the run time
#   depends on the list's length, which is O(n).

#   List has a cycle:
#   We break down the movement of the slow pointer into two
#   steps, the non-cyclic part and the cyclic part:
#       1. The slow pointer takes "non-cyclic length" steps to enter the cycle.
#          At this point, the fast pointer has already reached the cycle.
#          number of iterations = non-cyclic length = n
#       2. Both pointers are now in the cycle. Consider two runners running
#          in a cycle - the fast runner moves 2 steps while the slow runner
#          moves 1 steps at a time. Since the speed difference is 1, it takes
#          distance between the 2 runners / difference of speed
#          loops for the fast runner to catch up with the slow runner.
#          As the distance is at most "cyclic length k" and the speed
#          difference is 1, we conclude that 
#          number of iterations = almost "cyclic length k"

#   Therefore, the worst case time complexity is O(n + k), which is O(n).

# space: O(1) - We only use two nodes (slow an fast).

# Algorithm:
# The space complexity can be reduced to O(1) by considering two pointers
# at different speed - a slow pointer and a fast pointer.
# The slow pointer moves one step at a time while
# the fast pointer moves two steps at a time.

# If there is no cycle in the list, the fast pointer will eventually reach
# the end and we can return false in this case.

# Now consider a cyclic list and imagine the slow and fast pointers are
# two runners racing around a circle track. The fast runner will eventually
# meet the slow runner. Why?
# Consider this case (we name it case A) - The fast runner is just
# one step behind the slow runner. In the next iteration, they
# both increment one and two steps respectively and meet each other.

# How about other cases? For example, we have not considered cases where
# the fast runner is two or three steps behind the slow runner yet.
# This is simple, because in the next or next's next iteration, this
# case will be reduced to case A mentioned above.
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


