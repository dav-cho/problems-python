##
#### Flatten a Multilevel Doubly Linked List (medium)
#########################################################

# You are given a doubly linked list which in addition to the next and
# previous pointers, it could have a child pointer, which may or may not point
# to a separate doubly linked list. These child lists may have one or more
# children of their own, and so on, to produce a multilevel data structure,
# as shown in the example below.

# Flatten the list so that all the nodes appear in a single-level,
# doubly linked list. You are given the head of the first level of the list.

# Example 1:
# Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# Output: [1,2,3,7,8,11,12,9,10,4,5,6]

# Explanation:
# The multilevel linked list in the input is as follows:

# After flattening the multilevel linked list it becomes:

# Example 2:
# Input: head = [1,2,null,3]
# Output: [1,3,2]

# Explanation:

# The input multilevel linked list is as follows:

#   1---2---NULL
#   |
#   3---NULL

# Example 3:
# Input: head = []
# Output: []

# How multilevel linked list is represented in test case:

# We use the multilevel linked list from Example 1 above:

#  1---2---3---4---5---6--NULL
#          |
#          7---8---9---10--NULL
#              |
#              11--12--NULL

# The serialization of each level is as follows:

# [1,2,3,4,5,6,null]
# [7,8,9,10,null]
# [11,12,null]

# To serialize all levels together we will add nulls in each level to signify
# no node connects to the upper node of the previous level. The serialization
# becomes:

# [1,2,3,4,5,6,null]
# [null,null,7,8,9,10,null]
# [null,11,12,null]

# Merging the serialization of each level and removing trailing nulls we obtain:

# [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
 
# Constraints:
# The number of Nodes will not exceed 1000.
# 1 <= Node.val <= 105

################################################################################

## Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


## simple
#############
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return

        curr = head
        while curr:
            if not curr.child:
                curr = curr.next
                continue

            child_tail = curr.child
            while child_tail.next:
                child_tail = child_tail.next

            if curr.next:
                curr.next.prev = child_tail
            child_tail.next = curr.next
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None

        return head


## stack
############
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return

        sentinel = Node(None, None, head, None)
        stack = [head]
        prev = sentinel
        while stack:
            curr = stack.pop()
            curr.prev = prev
            prev.next = curr

            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
            prev = curr

        sentinel.next.prev = None
        return sentinel.next


### dfs recursive
#####################
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return

        sentinel = Node(None, None, head, None)
        self.flatten_dfs(sentinel, head)
        sentinel.next.prev = None
        
        return sentinel

    def flatten_dfs(self, prev, curr):
        if not curr:
            return prev

        curr.prev, prev.next = prev, curr
        temp_next = curr.next
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None

        return self.flatten_dfs(tail, temp_next)


## dfs iterative
####################
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return

        sentinel = Node(None, None, head, None)
        prev = sentinel

        stack = [head]
        while stack:
            curr = stack.pop()
            prev.next, curr.prev = curr, prev

            if curr.next:
                stack.append(curr.next)
            if curr.child:
                stack.append(curr.child)
                curr.child = None

            prev = curr

        sentinel.next.prev = None

        return sentinel.next


## Tests
############

def test1():
    pass


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
                head1 = Node(test[0][0])
            if not test[1]:
                head2 = []
            else:
                head2 = Node(test[1][0])

            current1 = head1
            for i in range(1, len(test[0])):
                current1.next = Node(test[0][i])
                current1 = current1.next
            current2 = head2
            for i in range(1, len(test[1])):
                current2.next = Node(test[1][i])
                current2 = current2.next

            print_LL(head1, 'l1:')
            print_LL(head2, 'l2:')
            solution = Solution()
            result = solution.add_two_numbers(head1, head2)
            print_LL(result, 'result:')

    return run()


def print_LL(head, msg="print_LL"):
    linked_list = []

    while head:
        linked_list.append(head.val)
        head = head.next

    print(msg, linked_list)
        

## LeetCode Solutions
#########################

## Approach 1: DFS by Recursion
###################################
# time: O(n) - where n is the number of nodes in the list. The DFS algorithm
#              traverses each node once and only once.
# space: O(n) - where n is the number of nodes in the list. In the worst case,
#               the binary tree might be extremely unbalanced (i.e. the tree
#               leans to the left), which corresponds to the case where nodes
#               are chained with each other only with the child pointers. In
#               this case, the recursive calls would pile up, and it would
#               take n space in the function call stack.
class Solution(object):

    def flatten(self, head):
        if not head:
            return head

        # pseudo head to ensure the `prev` pointer is never none
        pseudoHead = Node(None, None, head, None)
        self.flatten_dfs(pseudoHead, head)

        # detach the pseudo head from the real head
        pseudoHead.next.prev = None
        return pseudoHead.next


    def flatten_dfs(self, prev, curr):
        """ return the tail of the flatten list """
        if not curr:
            return prev

        curr.prev = prev
        prev.next = curr

        # the curr.next would be tempered in the recursive function
        tempNext = curr.next
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None
        return self.flatten_dfs(tail, tempNext)


## Approach 2: DFS by Iteration
###################################
# time: O(n) - The iterative solution has the same time complexity as
#              the recursive.
# space: O(n) - Again, the iterative solution has the same space complexity
#               as the recursive one.
class Solution(object):
    def flatten(self, head):
        if not head:
            return

        pseudoHead = Node(0,None,head,None)
        prev = pseudoHead

        stack = []
        stack.append(head)

        while stack:
            curr = stack.pop()

            prev.next = curr
            curr.prev = prev

            if curr.next:
                stack.append(curr.next)
 
            if curr.child:
                stack.append(curr.child)
                # don't forget to remove all child pointers.
                curr.child = None

            prev = curr
        # detach the pseudo head node from the result.
        pseudoHead.next.prev = None
        return pseudoHead.next


