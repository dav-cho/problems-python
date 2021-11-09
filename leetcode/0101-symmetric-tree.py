##
#### Symmetric Tree (easy)
##############################

# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).

# Example 1:
#           1
#       2       2
#     3   4   4   3
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
#           1
#       2       2
#         3       3
# Input: root = [1,2,2,null,3,null,3]
# Output: false
 
# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100

# Follow up: Could you solve it both recursively and iteratively?

################################################################################

## Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


## recursive
################
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            
            outside = helper(a.left, b.right)
            inside = helper(a.right, b.left)
            
            return outside and inside
        
        return helper(root, root)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(node_a, node_b):
            if not node_a and not node_b:
                return True
            if not node_a or not node_b:
                return False
            if node_a.val != node_b.val:
                return False
            
            left = helper(node_a.left, node_b.right)
            right = helper(node_a.right, node_b.left)
            
            return left and right
        
        return helper(root, root)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(node_a, node_b):
            if not node_a and not node_b:
                return True
            if not node_a or not node_b:
                return False
            
            left = helper(node_a.left, node_b.right)
            right = helper(node_a.right, node_b.left)
            
            return node_a.val == node_b.val and left and right
        
        return helper(root, root)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_mirror(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False

            left = is_mirror(node1.left, node2.right)
            right = is_mirror(node2.right, node1.left)

            return node1.val == node2.val and left and right
        
        return is_mirror(root, root)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_mirror(root, root)
    
    def is_mirror(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        
        left = self.is_mirror(node1.left, node2.right)
        right = self.is_mirror(node2.right, node1.left)
        
        return node1.val == node2.val and left and right


## iterative
################
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [(root, root)]
        
        while stack:
            a, b = stack.pop()
            
            if not a and not b:
                continue
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            
            stack.append((a.left, b.right))
            stack.append((a.right, b.left))
            
        return True


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [(root, root)]
        
        while stack:
            node_a, node_b = stack.pop()
            
            if not node_a and not node_b:
                continue
            if not node_a or not node_b:
                return False
            if node_a.val != node_b.val:
                return False
            
            stack.append((node_a.left, node_b.right))
            stack.append((node_a.right, node_b.left))
            
        return True


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = [root, root]

        while queue:
            node1 = queue.pop()
            node2 = queue.pop()
            
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            
            queue.append(node1.left)
            queue.append(node2.right)
            
            queue.append(node1.right)
            queue.append(node2.left)

        return True


## Tests
############


## LeetCode Solutions
#########################

## Approach 1: Recursive
############################
# time: O(n) - Because we traverse the entire input tree once, the total run
#              time is O(n), where n is the total number of nodes in the tree.
# space: O(n) - The number of recursive calls is bound by the height of the
#               tree. In the worst case, the tree is linear and the height is in
#               O(n). Therefore, space complexity due to recursive calls on the
#               stack is O(n) in the worst case.

## Java
#public boolean isSymmetric(TreeNode root) {
#    return isMirror(root, root);
#}
#
#public boolean isMirror(TreeNode t1, TreeNode t2) {
#    if (t1 == null && t2 == null) return true;
#    if (t1 == null || t2 == null) return false;
#    return (t1.val == t2.val)
#        && isMirror(t1.right, t2.left)
#        && isMirror(t1.left, t2.right);
#}


## Approach 2: Iterative
############################
# time: O(n) - Because we traverse the entire input tree once, the total run
#              time is O(n), where nn is the total number of nodes in the tree.
# space: O(n) - There is additional space required for the search queue. In the
#               worst case, we have to insert O(n) nodes in the queue.
#               Therefore, space complexity is O(n).

## Java
#public boolean isSymmetric(TreeNode root) {
#    Queue<TreeNode> q = new LinkedList<>();
#    q.add(root);
#    q.add(root);
#    while (!q.isEmpty()) {
#        TreeNode t1 = q.poll();
#        TreeNode t2 = q.poll();
#        if (t1 == null && t2 == null) continue;
#        if (t1 == null || t2 == null) return false;
#        if (t1.val != t2.val) return false;
#        q.add(t1.left);
#        q.add(t2.right);
#        q.add(t1.right);
#        q.add(t2.left);
#    }
#    return true;
#}

