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


################################################################################


## first attempt (wrong answer)
##############################
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        
        while head:
            if stack and head.val == stack[-1]:
                stack.pop()
            else:
                stack.append(head.val)
                
            head = head.next
            
        return len(stack) == 0


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
        pass


## Tests
#############


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


## LeetCode Solutions
#########################

## Approach 1: Copy into Array List and then Use Two Pointer Technique
##########################################################################
# Time: O(n) - Where n is the number of nodes in the Linked List.
# - In the first part, we're copying a Linked List into an Array List. Iterating
#   down a Linked List in sequential order is O(n), and each of the n writes to
#   the ArrayList is O(1). Therefore, the overall cost is O(n).
# - In the second part, we're using the two pointer technique to check whether
#   or not the Array List is a palindrome. Each of the n values in the Array
#   list is accessed once, and a total of O(n/2) comparisons are done.
#   Therefore, the overall cost is O(n). The Python trick (reverse and list
#   comparison as a one liner) is also O(n).
# - This gives O(2n)=O(n) because we always drop the constants.

# Space complexity : O(n) - where n is the number of nodes in the Linked List.
# - We are making an Array List and adding n values to it.

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]


## Approach 2: Recursive (Advanced)
#######################################
# Time: O(n) - Where n is the number of nodes in the Linked List.
# - The recursive function is run once for each of the n nodes, and the body of
#   the recursive function is O(1). Therefore, this gives a total of O(n).

# Space: O(n) - Where n is the number of nodes in the Linked List.
# - I hinted at the start that this is not using O(1) space. This might seem
#   strange, after all we aren't creating any new data structures. So, where is
#   the O(n) extra memory we're using? Understanding what is happening here
#   requires understanding how the computer runs a recursive function.
# - Each time a function is called within a function, the computer needs to keep
#   track of where it is up to (and the values of any local variables) in the
#   current function before it goes into the called function. It does this by
#   putting an entry on something called the runtime stack, called a stack
#   frame. Once it has created a stack frame for the current function, it can
#   then go into the called function. Then once it is finished with the called
#   function, it pops the top stack frame to resume the function it had been in
#   before the function call was made.
# - Before doing any palindrome checking, the above recursive function creates
#   n of these stack frames because the first step of processing a node is to
#   process the nodes after it, which is done with a recursive call. Then once
#   it has the nn stack frames, it pops them off one-by-one to process them.
# - So, the space usage is on the runtime stack because we are creating n stack
#   frames. Always make sure to consider what's going on the runtime stack when
#   analyzing a recursive function. It's a common mistake to forget to.

# Not only is this approach still using O(n) space, it is worse than the first
# approach because in many languages (such as Python), stack frames are large,
# and there's a maximum runtime stack depth of 1000 (you can increase it, but
# you risk causing memory errors with the underlying interpreter). With every
# node creating a stack frame, this will greatly limit the maximum Linked List
# size the algorithm can handle.

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


## Approach 3: Reverse Second Half In-place
###############################################
# Time: O(n) - Where n is the number of nodes in the Linked List.
# - Similar to the above approaches. Finding the middle is O(n), reversing a
#   list in place is O(n), and then comparing the 2 resulting Linked Lists is
#   also O(n).

# Space: O(1)
# - We are changing the next pointers for half of the nodes. This was all memory
#   that had already been allocated, so we are not using any extra memory and
#   therefore it is O(1).
# - I have seen some people on the discussion forum saying it has to be O(n)
#   because we're creating a new list. This is incorrect, because we are
#   changing each of the pointers one-by-one, in-place. We are not needing to
#   allocate more than O(1) extra memory to do this work, and there is O(1)
#   stack frames going on the stack. It is the same as reversing the values in
#   an Array in place (using the two-pointer technique).

# The downside of this approach is that in a concurrent environment (multiple
# threads and processes accessing the same data), access to the Linked List by
# other threads or processes would have to be locked while this function is
# running, because the Linked List is temporarily broken. This is a limitation
# of many in-place algorithms though.

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


