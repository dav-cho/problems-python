##
#### Serialize and Deserialize Binary Tree (hard)
#####################################################

# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should
# work. You just need to ensure that a binary tree can be serialized to a string# and this string can be deserialized to the original tree structure.

# Clarification: The input/output format is the same as how LeetCode serializes
# a binary tree. You do not necessarily need to follow this format, so please
# be creative and come up with different approahes yourself.

# Example 1:
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]

# Example 4:
# Input: root = [1,2]
# Output: [1,2]
 
# Constraints:
 
# The number of nodes in the tree is in the range [0, 104].
# -1000 <= Node.val <= 1000c

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

## recursive
################
class Codec:
    def serialize(self, root):
        def helper(node, result):
            if not node:
                result.append(None)
            else:
                result = helper(node.left, result)
                result = helper(node.right, result)
                result.append(node.val)
            return result
        
        return helper(root, [])
        

    def deserialize(self, data):
        def helper(arr):
            if arr[-1] is None:
                return arr.pop()
            
            root = TreeNode(arr.pop())
            root.right = helper(arr)
            root.left = helper(arr)
            return root
        
        return helper(data)


class Codec:
    def serialize(self, root):
        def serialize_recursive_helper(node, result):
            if node is None:
                result.append(None)
            else:
                result = serialize_recursive_helper(node.left, result)
                result = serialize_recursive_helper(node.right, result)
                result.append(node.val)
            return result

        return serialize_recursive_helper(root, [])

    def deserialize(self, data):
        def deserialize_recursive_helper(arr):
            if arr[-1] is None:
                return arr.pop()

            root = TreeNode(arr.pop())
            root.right = deserialize_recursive_helper(arr)
            root.left = deserialize_recursive_helper(arr)
            return root

        return deserialize_recursive_helper(data)


class Codec:
    def serialize(self, root):
        def serialize_recursive_helper(node, result):
            if node is None:
                result.append(None)
            else:
                result.append(node.val)
                result = serialize_recursive_helper(node.left, result)
                result = serialize_recursive_helper(node.right, result)
            return result

        return serialize_recursive_helper(root, [])

    def deserialize(self, data):
        def deserialize_recursive_helper(arr):
            if arr[-1] is None:
                return arr.pop()

            root = TreeNode(arr.pop())
            root.left = deserialize_recursive_helper(arr)
            root.right = deserialize_recursive_helper(arr)
            return root

        data.reverse()
        return deserialize_recursive_helper(data) 


class Codec:
    def serialize(self, root):
        def serialize_recursive_helper(node, result):
            if node is None:
                result.append(None)
            else:
                result.append(node.val)
                result = serialize_recursive_helper(node.left, result)
                result = serialize_recursive_helper(node.right, result)
            return result
        
        return serialize_recursive_helper(root, [])

    def deserialize(self, data):
        def deserialize_recursive_helper(arr):
            if arr[0] is None:
                return arr.pop(0)
                
            root = TreeNode(arr[0])
            arr.pop(0)
            root.left = deserialize_recursive_helper(arr)
            root.right = deserialize_recursive_helper(arr)
            return root

        return deserialize_recursive_helper(data)


class Codec:
    def serialize(self, root):
        def serialize_recursive_helper(node, string):
            if node is None:
                string += 'None,'
            else:
                string += str(node.val) + ','
                string = serialize_recursive_helper(node.left, string)
                string = serialize_recursive_helper(node.right, string)
            return string
        
        return serialize_recursive_helper(root, '')

    def deserialize(self, data):
        def deserialize_recursive_helper(arr):
            if arr[0] == 'None':
                return arr.pop(0)
                
            root = TreeNode(arr[0])
            arr.pop(0)
            root.left = deserialize_recursive_helper(arr)
            root.right = deserialize_recursive_helper(arr)
            return root

        data_list = data.split(',')
        root = deserialize_recursive_helper(data_list)
        return root


## Tests
############

test1 = [1,2,3,null,null,4,5]   # [1,2,3,null,null,4,5]
test2 = []                      # []
test3 = [1]                     # [1]
test4 = [1,2]                   # [1,2]
test5 = [1,2,2]                 # [1,2,2]
test6 = [1,2,3,null,null,4,5]   # [1,2,3,null,null,4,5]


## LeetCode Solutions
#########################


## Approach 1: Depth First Search (DFS)
###########################################
# Time: O(N)
# in both serialization and deserialization functions, we visit each node
# exactly once, thus the time complexity is O(N), where NN is the number of
# nodes, i.e. the size of tree.

# Space: O(N)
# In both serialization and deserialization functions, we keep the entire tree,
# either at the beginning or at the end.
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


