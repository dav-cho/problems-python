##
#### Serialize and Deserialize Binary Tree (hard)
#####################################################

# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes
# a binary tree. You do not necessarily need to follow this format, so please
# be creative and come up with different approaches yourself.

# Example 1:
#       1
#    2     3
#        4   5
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

# Example 2:
# Input: root = []
# Output: []
 
# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -1000 <= Node.val <= 1000

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

################################################################################


## Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


## recursive preorder dfs *best
##################################
class Codec:
    def serialize(self, root):
        def dfs_preorder(node, vals):
            if node:
                vals.append(str(node.val))
                dfs_preorder(node.left, vals)
                dfs_preorder(node.right, vals)
            else:
                vals.append('None')
                
            return vals
        
        return ','.join(dfs_preorder(root, []))

    def deserialize(self, data):
        def dfs_preorder(queue):
            val = next(queue)
            
            if val == 'None':
                return
            
            root = TreeNode(int(val))
            root.left = dfs_preorder(queue)
            root.right = dfs_preorder(queue)
            
            return root
        
        return dfs_preorder(iter(data.split(',')))


class Codec:
    def serialize(self, root):
        def helper(node, vals):
            if node:
                vals.append(str(node.val))
                helper(node.left, vals)
                helper(node.right, vals)
            else:
                vals.append('None')
            
            return vals
        
        return ','.join(helper(root, []))

    def deserialize(self, data):
        def helper(queue):
            val = next(queue)
            if val == 'None':
                return
            
            node = TreeNode(int(val))
            node.left = helper(queue)
            node.right = helper(queue)
            return node
        
        return helper(iter(data.split(',')))


class Codec:
    def serialize(self, root):
        vals = []
        
        def helper(node):
            if node:
                vals.append(str(node.val))
                helper(node.left)
                helper(node.right)
            else:
                vals.append('None')
            
            return vals
        
        return ','.join(helper(root))

    def deserialize(self, data):
        vals = iter(data.split(','))
        
        def helper():
            val = next(vals)
            if val == 'None':
                return
            
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            
            return node
        
        return helper()


## dfs
##############################
class Codec:
    def serialize(self, root):
        def dfs_preorder(node, string):
            if node:
                string += str(node.val) + ','
                string = dfs_preorder(node.left, string)
                string = dfs_preorder(node.right, string)
            else:
                string += 'None,'
                
            return string
        
        return dfs_preorder(root, '')

    def deserialize(self, data):
        def dfs_preorder(queue):
            if queue[0] == 'None':
                queue.popleft()
                return
            
            root = TreeNode(queue.popleft())
            root.left = dfs_preorder(queue)
            root.right = dfs_preorder(queue)
            
            return root
        
        return dfs_preorder(deque(data.split(',')))


class Codec:
    def serialize(self, root):
        def helper(node, string):
            if not node:
                string += 'None,'
            else:
                string += str(node.val) + ','
                string = helper(node.left, string)
                string = helper(node.right, string)
            return string
        return helper(root, '')

    def deserialize(self, data):
        def helper(queue):
            if queue[0] == 'None':
                queue.popleft()
                return
            
            root = TreeNode(queue.popleft())
            root.left = helper(queue)
            root.right = helper(queue)
            return root
        return helper(deque(data.split(',')))


class Codec:
    def serialize(self, root):
        def helper(node, string):
            if not node:
                string += 'None,'
            else:
                string += f"{str(node.val)},"
                string = helper(node.left, string)
                string = helper(node.right, string)
            return string
        return helper(root, '')
            

    def deserialize(self, data):
        def helper(lst):
            if lst[0] == 'None':
                lst.pop(0)
                return None
            
            root = TreeNode(lst.pop(0))
            root.left = helper(lst)
            root.right = helper(lst)
            return root
        return helper(data.split(','))


class Codec:
    def serialize(self, root):
        def helper(root, string):
            if not root:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = helper(root.left, string)
                string = helper(root.right, string)
            return string
        return helper(root, '')
            

    def deserialize(self, data):
        def helper(lst):
            if lst[0] == 'None':
                lst.pop(0)
                return None
            
            root = TreeNode(lst.pop(0))
            root.left = helper(lst)
            root.right = helper(lst)
            return root
        
        data_list = data.split(',')
        root = helper(data_list)
        return root


## discuss solutions
##############################

## recursive preorder dfs
##############################
class Codec:
    def serialize(self, root):
        vals = []
        
        def helper(node):
            if node:
                vals.append(str(node.val))
                helper(node.left)
                helper(node.right)
            else:
                vals.append('None')
                
            return vals
        
        return ','.join(helper(root))

    def deserialize(self, data):
        def helper():
            val = next(vals)
            if val == 'None':
                return
            
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            
            return node
        
        vals = iter(data.split(','))
        return helper()


## hybrid solutions (LC + Discuss)
######################################
class Codec:
    def serialize(self, root):
        def helper(node, string):
            if not node:
                string += 'None,'
            else:
                string += str(node.val) + ','
                string = helper(node.left, string)
                string = helper(node.right, string)
            return string
        
        return helper(root, '')

    def deserialize(self, data):
        lst = iter(data.split(','))
        
        def helper():
            val = next(lst)
            if val == 'None':
                return
            
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node
        
        return helper()


class Codec:
    def serialize(self, root):
        def helper(node, string):
            if not node:
                string += 'None,'
            else:
                string += str(node.val) + ','
                string = helper(node.left, string)
                string = helper(node.right, string)
            return string
        return helper(root, '')

    def deserialize(self, data):
        lst = iter(data.split(','))
        
        def helper():
            val = next(lst)
            if val == 'None':
                return
            
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            
            return node
        
        return helper()


## 
##############################
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )
        self.assertCountEqual()


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Depth First Search (DFS)
###########################################
# Time: O(N) - In both serialization and deserialization functions, we visit
#              each node exactly once, thus the time complexity is O(N), where
#              N is the number of nodes, i.e. the size of tree.
# Space: O(N) - In both serialization and deserialization functions, we keep
#               the entire tree, either at the beginning or at the end,
#               therefore, the space complexity is O(N).
class Codec:

    def serialize(self, root):
        """ Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        def rserialize(root, string):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string
        
        return rserialize(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None
                
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root


