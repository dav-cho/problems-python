##
#### 297. Serialize and Deserialize Binary Tree (hard)
##########################################################



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

