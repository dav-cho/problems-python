##
#### 142. Linked List Cycle II (medium)
###########################################


## Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


## hash table
#################
class Solution:
    def detect_cycle(self, head: ListNode) -> ListNode:
        visited = set()

        while head:
            if head in visited:
                return head

            visited.add(head)
            head = head.next

        return None


## two pointer - floyd's algorithm
######################################
class Solution:
    def get_intersect(self, head):
        slow = fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return slow

        return None

    def detect_cycle(self, head: ListNode) -> ListNode:
        if not head:
            return None

        intersect = self.get_intersect(head)
        if not intersect:
            return None

        pointer1 = head
        pointer2 = intersect
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer1


## two pointer - floyd's algorithm 2
########################################
class Solution:
    def detect_cycle(self, head):
        try:
            slow = head
            fast = head.next
            while fast is not slow:
                slow = slow.next
                fast = fast.next.next
        except:
            return None

        slow = slow.next
        while head is not slow:
            head = head.next
            slow = slow.next

        return head
