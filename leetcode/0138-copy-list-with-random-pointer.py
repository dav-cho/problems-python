##
#### Copy List with Random Pointer (medium)
###############################################

# A linked list of length n is given such that each node contains an additional
# random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly
# n brand new nodes, where each new node has its value set to the value of its
# corresponding original node. Both the next and random pointer of the new
# nodes should point to new nodes in the copied list such that the pointers in
# the original list and copied list represent the same list state. None of the
# pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where
# X.random --> Y, then for the corresponding two nodes x and y in the copied
# list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes.
# Each node is represented as a pair of [val, random_index] where:

# - val: an integer representing Node.val
# - random_index: the index of the node (range from 0 to n-1) that the random
#   pointer points to, or null if it does not point to any node.

# Your code will only be given the head of the original linked list.

# Example 1:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# Example 2:
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]

# Example 3:
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]

# Example 4:
# Input: head = []
# Output: []
# Explanation: The given linked list is empty (null pointer), so return null.
 
# Constraints:
# 0 <= n <= 1000
# -10000 <= Node.val <= 10000
# Node.random is null or is pointing to some node in the linked list.

################################################################################

## Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

## recursive
################
class Solution:
    def __init__(self):
        self.visited = {}
        
    def copy_random_list(self, head: Node) -> Node:
        if not head:
            return
        
        if head in self.visited:
            return self.visited[head]
        
        new = Node(head.val)
        self.visited[head] = new
        
        new.next = self.copy_random_list(head.next)
        new.random = self.copy_random_list(head.random)
        
        return new


## iterative
################
class Solution:
    def __init__(self):
        self.visited = {}
        
    def get_clone(self, node):
        if not node:
            return
        if node not in self.visited:
            self.visited[node] = Node(node.val)
            
        return self.visited[node]
        
    def copy_random_list(self, head: Node) -> Node:
        if not head:
            return
        
        old = head
        new = Node(old.val)
        self.visited[old] = new
        
        while old:
            new.next = self.get_clone(old.next)
            new.random = self.get_clone(old.random)
            
            old = old.next
            new = new.next
            
        return self.visited[head]


## iterative with O(1) space
################################
class Solution:
    def copy_random_list(self, head: Node) -> Node:
        if not head:
            return
        
        curr = head
        while curr:
            new = Node(curr.val)
            new.next = curr.next
            curr.next = new
            curr = new.next
        
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        old_curr = head
        new_curr = new_head = head.next
        while old_curr:
            old_curr.next = old_curr.next.next
            if new_curr.next:
                new_curr.next = new_curr.next.next
            old_curr = old_curr.next
            new_curr = new_curr.next
        
        return new_head


## Tests
############

test1 = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
# [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]

test2 = [[1, 1], [2, 1]]
# [[1, 1], [2, 1]]

test3 = [[3, None], [3, 0], [3, None]]
# [[3,None],[3,0],[3,None]]

test4 = []
# []

tests = (
    test1,
    test2,
    test3,
    test4,
)


def test(*args):
    count = 1

    def run():
        for test in args:
            nonlocal count
            print(f"~ test{count}")
            count += 1

            if not test:
                head = []
            else:
                seen = []
                prev = head = None

                for i in range(len(test)):
                    new = Node(test[i][0])
                    seen.append(new)

                    if not head:
                        head = new
                    if prev:
                        prev.next = new
                    prev = new

                curr = head
                for i in range(len(test)):
                    if test[i][1] is not None:
                        curr.random = seen[test[i][1]]
                    curr = curr.next

            print_LL(head, 'list')

            solution = Solution()
            result = solution.copy_random_list(head)

            print_LL(result, 'result')


    return run()


def print_LL(head, msg="print_LL"):
    arr, seen = [], set()

    temp = [None, None]
    while head:
        if head in seen:
            break

        temp[0] = head.val
        temp[1] = head.random.val if head.random else None
        arr.append(temp)
        seen.add(head)
        temp = [None, None]
        head = head.next

    print(msg, arr)


test(*tests)


## LeetCode Solutions
#########################

## Approach 1: Recursive
############################
# time: O(n) - where n is the number of nodes in the linked list.
# space: O(n) - If we look closely, we have the recursion stack and we also
#               have the space complexity to keep track of nodes already
#               cloned i.e. using the visited dictionary. But asymptotically,
#               the complexity is O(n)
class Solution(object):
    """
    :type head: Node
    :rtype: Node
    """
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}

    def copyRandomList(self, head):

        if head == None:
            return None

        # If we have already processed the current node, then we simply return the cloned version of it.
        if head in self.visitedHash:
            return self.visitedHash[head]

        # create a new node
        # with the value same as old node.
        node = Node(head.val, None, None)

        # Save this value in the hash map. This is needed since there might be
        # loops during traversal due to randomness of random pointers and this would help us avoid them.
        self.visitedHash[head] = node

        # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
        # Thus we have two independent recursive calls.
        # Finally we update the next and random pointers for the new node created.
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node


## Approach 2: Iterative with O(N) Space
############################################
# time: O(n) - we make one pass over the original list.
# space: O(n) - we have a dictionary containing mapping from old list nodes to
#               new list nodes. Since they are n nodes, we have O(n) space
#               coplexity
class Solution(object):
    def __init__(self):
        # Creating a visited dictionary to hold old node reference as "key" and new node reference as the "value"
        self.visited = {}

    def getClonedNode(self, node):
        # If node exists then
        if node:
            # Check if its in the visited dictionary          
            if node in self.visited:
                # If its in the visited dictionary then return the new node reference from the dictionary
                return self.visited[node]
            else:
                # Otherwise create a new node, save the reference in the visited dictionary and return it.
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]
        return None

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if not head:
            return head

        old_node = head
        # Creating the new head node.       
        new_node = Node(old_node.val, None, None)
        self.visited[old_node] = new_node

        # Iterate on the linked list until all nodes are cloned.
        while old_node != None:

            # Get the clones of the nodes referenced by random and next pointers.
            new_node.random = self.getClonedNode(old_node.random)
            new_node.next = self.getClonedNode(old_node.next)

            # Move one step ahead in the linked list.
            old_node = old_node.next
            new_node = new_node.next

        return self.visited[head]


## Approach 3: Iterative with O(1) Space
############################################
# time: O(n)
# space: O(1)
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        # Creating a new weaved list of original and copied nodes.
        ptr = head
        while ptr:

            # Cloned node
            new_node = Node(ptr.val, None, None)

            # Inserting the cloned node just next to the original node.
            # If A->B->C is the original linked list,
            # Linked list after weaving cloned nodes would be A->A'->B->B'->C->C'
            new_node.next = ptr.next
            ptr.next = new_node
            ptr = new_node.next

        ptr = head

        # Now link the random pointers of the new nodes created.
        # Iterate the newly created list and use the original nodes random pointers,
        # to assign references to random pointers for cloned nodes.
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        # Unweave the linked list to get back the original linked list and the cloned list.
        # i.e. A->A'->B->B'->C->C' would be broken to A->B->C and A'->B'->C'
        ptr_old_list = head # A->B->C
        ptr_new_list = head.next # A'->B'->C'
        head_new = head.next
        while ptr_old_list:
            ptr_old_list.next = ptr_old_list.next.next
            ptr_new_list.next = ptr_new_list.next.next if ptr_new_list.next else None
            ptr_old_list = ptr_old_list.next
            ptr_new_list = ptr_new_list.next
        return head_new

