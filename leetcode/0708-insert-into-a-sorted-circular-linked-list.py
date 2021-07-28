##
#### Insert into a Sorted Circular Linked List (medium)
###########################################################

# Given a Circular Linked List node, which is sorted in ascending order, write
# a function to insert a value insertVal into the list such that it remains a
# sorted circular list. The given node can be a reference to any single
# node in the list and may not necessarily be the smallest value in the
# circular list.

# If there are multiple suitable places for insertion, you may choose any
# place to insert the new value. After the insertion, the circular list should
# remain sorted.

# If the list is empty (i.e., the given node is null), you should create a new
# single circular list and return the reference to that single node.
# Otherwise, you should return the originally given node.

# Example 1:

# 3 -> 4 -> 1 -> (3)

#   1 ------
#   |       |
#   4 <---- 3
#
# Input: head = [3,4,1], insertVal = 2
# Output: [3,4,1,2]
# Explanation: In the figure above, there is a sorted circular list of three
# elements. You are given a reference to the node with value 3, and we need
# to insert 2 into the list. The new node should be inserted between node 1
# and node 3. After the insertion, the list should look like this, and we
# should still return node 3.

# Example 2:
# Input: head = [], insertVal = 1
# Output: [1]
# Explanation: The list is empty (given head is null). We create a new single
# circular list and return the reference to that single node.

# Example 3:
# Input: head = [1], insertVal = 0
# Output: [1,0]

# Constraints:
# 0 <= Number of Nodes <= 5 * 104
# -106 <= Node.val, insertVal <= 106

################################################################################

## Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

## TODO: find min and max
#######################
class Solution:
    def insert(self, head: Node, insertVal: int) -> Node:
        new = Node(insertVal)

        if not head:
            new.next = new
            return new
        if head == head.next:
            head.next, new.next = new, head
            return head

        mn = mx = head.val
        curr = head.next
        while True:
            if curr == head:
                break
            mn = min(mn, curr.val)
            mx = max(mx, curr.val)
            curr = curr.next
        
        prev = head
            
        new.next, prev.next = prev.next, new

        return head


## two pointer iteration 1
##############################
class Solution:
    def insert(self, head: Node, insertVal: int) -> Node:
        new = Node(insertVal)
        
        if not head:
            new.next = new
            return new
        
        prev = head
        while True:
            if prev.val <= insertVal <= prev.next.val:
                break
            if prev.val > prev.next.val:
                if insertVal >= prev.val or insertVal <= prev.next.val:
                    break
            if prev.next == head:
                break
            prev = prev.next
                
        new.next, prev.next = prev.next, new
        
        return head


## two pointer iteration 2
##############################
class Solution:
    def insert(self, head: Node, insertVal: int) -> Node:
        new = Node(insertVal)
        
        if not head:
            new.next = new
            return new
        
        prev = head
        while True:
            if prev.val <= insertVal <= prev.next.val:
                break
            if prev.val > prev.next.val:
                if insertVal >= prev.val or insertVal <= prev.next.val:
                    break
                    
            prev = prev.next
            if prev == head:
                break
                
        new.next, prev.next = prev.next, new
        
        return head


## Tests
############

test1 = ([3, 4, 1], 2)      # [3, 4, 1, 2]
test2 = ([], 1)             # [1]
test3 = ([1], 0)            # [1, 0]
test4 = ([3, 3, 3], 0)      # [3, 3, 3, 0]
test5 = ([1, 3, 5], 4)      # [1, 3, 4, 5]
test6 = ([3, 5, 1], 0)      # [3, 5, 0, 1]

tests = (
    test1,
    test2,
    test3,
    test4,
    test5,
    test6,
    ([3, 5, 1], 0),
    ([3, 5, 1], 6),
    ([3, 3, 3], 0),
    ([3, 3, 3], 6),
    ([3, 4, 1], 2),
)


def test(*args):
    count = 1

    def run():
        for test in args:
            nonlocal count
            print(f"~ test{count}")
            count += 1

            linked_list, val = test

            if not linked_list:
                head = []
            else:
                head = Node(linked_list[0])
                curr = head
                for i in range(1, len(linked_list)):
                    curr.next = Node(linked_list[i])
                    curr = curr.next

                curr.next = head

            print('insert', val)
            print_LL(head, 'list')

            solution = Solution()
            result = solution.insert(head, val)

            print_LL(result, 'result')


    return run()


def print_LL(head, msg="print_LL"):
    arr, seen = [], set()

    while head:
        if head in seen:
            break
        arr.append(head.val)
        seen.add(head)
        head = head.next

    print(msg, arr)


test(*tests)


## LeetCode Solutions
#########################

## Approach 1: Two-Pointers Iteration
#########################################
# time: O(N) - where N is the size of list. In the worst case, we would
#              iterate through the entire list.
# space: O(1) - It is a constant space solution.
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':

        if head == None:
            newNode = Node(insertVal, None)
            newNode.next = newNode
            return newNode
 
        prev, curr = head, head.next
        toInsert = False

        while True:
            
            if prev.val <= insertVal <= curr.val:
                # Case #1.
                toInsert = True
            elif prev.val > curr.val:
                # Case #2. where we locate the tail element
                # 'prev' points to the tail, i.e. the largest element!
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True

            if toInsert:
                prev.next = Node(insertVal, curr)
                # mission accomplished
                return head

            prev, curr = curr, curr.next
            # loop condition
            if prev == head:
                break
        # Case #3.
        # did not insert the node in the loop
        prev.next = Node(insertVal, curr)
        return head

