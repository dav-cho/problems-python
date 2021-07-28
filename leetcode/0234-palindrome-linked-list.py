##
#### Palindrome Linked List (easy)
######################################

# Given the head of a singly linked list, return true if it is a palindrome.

# Example 1:
# Input: head = [1,2,2,1]
# Output: true

# Example 2:
# Input: head = [1,2]
# Output: false
 
# Constraints:
# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
 
# Follow up: Could you do it in O(n) time and O(1) space?

################################################################################

## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


## use an array of the values and compare reversed array
############################################################
class Solution:
    def is_palindrome(self, head: ListNode) -> bool:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        return arr == arr[::-1]


## recursive
################
class Solution:
    def is_palindrome(self, head: ListNode) -> bool:
        self.front_pointer = head

        def recursively_check(curr=head):
            if curr:
                if not recursively_check(curr.next):
                    return False
                if self.front_pointer.val != curr.val:
                    return False

                self.front_pointer = self.front_pointer.next

            return True

        return recursively_check()


## reverse second half in place
###################################
class Solution:
    def is_palindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        left_end = self.end_left(head)
        right_start = self.reverse_list(left_end.next)

        result = True
        left = head
        right = right_start
        while result and right:
            if left.val != right.val:
                result = False

            left = left.next
            right = right.next

        left_end.next = self.reverse_list(right_start)

        return result

    def end_left(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse_list(self, head):
        prev = None
        curr = head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        return prev




## Tests
############

test1 = [1, 2, 2, 1]    # True
test2 = [1, 2]          # False

def test(*args):
    count = 1

    def run():
        for test in args:
            nonlocal count
            print("~ test", count)
            count += 1

            if not test:
                print('[]')
                continue

            head = ListNode(test[0])
            current = head

            for i in range(1, len(test)):
                current.next = ListNode(test[i])
                current = current.next

            print_LL(head)
            solution = Solution()
            result = solution.is_palindrome(head)
            print(result)

    return run()


def print_LL(head):
    linked_list = []

    while head:
        linked_list.append(head.val)
        head = head.next

    print(linked_list)
        

test(test1, test2)


## LeetCode Solutions
#########################

## Approach 1: Copy into Array List and then Use Two Pointer Technique
##########################################################################
# time: O(n) - where n is number of nodes in the linked list
# space: O(n) - we are making an array list and adding n values to it
class Solution:
    def is_palindrome(self, head: ListNode) -> bool:
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        
        return vals == vals[::-1]


## Approach 2:
################
# time: O(n) - Where n is number of nodes in linked list.
#              The recursive function is run once for each of the n nodes,
#              and the body of the recursive function is O(1). Therefore,
#              this gives a total of O(n).
# space: O(n) - recursion creates n stacks
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()


## Approach 3:
################
# time: O(n) - Similar to the above approaches. Finding the middle is O(n),
#              reversing a list in place is O(n), and then comparing the
#              2 resulting Linked Lists is also O(n).
# space: O(1) - We are changing the next pointers for half of the nodes.
#               This was all memory that had already been allocated, so we
#               are not using any extra memory and therefore it is O(1).

#               The downside of this approach is that in a concurrent
#               environment (multiple threads and processes accessing the
#               same data), access to the Linked List by other threads or
#               processes would have to be locked while this function is
#               running, because the Linked List is temporarily broken.
#               This is a limitation of many in-place algorithms though.
class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result    

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous


