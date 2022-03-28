##
#### 220. Contains Duplicate III (medium)
########################################


# abs(nums[i] - nums[j]) <= t
# abs(i - j) <= k


## buckets
##############################
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], k: int, t: int) -> bool:
        if t < 0:
            return False

        d = {}
        w = t + 1
        for i in range(len(nums)):
            m = nums[i] // w

            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True

            d[m] = nums[i]

            if i >= k:
                del d[nums[i - k] // w]

        return False


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], k: int, t: int) -> bool:
        if t < 0:
            return False

        buckets = {}
        w = t + 1
        for i in range(len(nums)):
            j = nums[i] // w

            if j in buckets:
                return True
            if j - 1 in buckets and abs(nums[i] - buckets[j - 1]) < w:
                return True
            if j + 1 in buckets and abs(nums[i] - buckets[j + 1]) < w:
                return True

            buckets[j] = nums[i]

            if i >= k:
                del buckets[nums[i - k] // w]

        return False


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], k: int, t: int) -> bool:
        if t < 0:
            return False

        buckets = {}
        w = t + 1
        for i in range(len(nums)):
            bucket = nums[i] // w

            if bucket in buckets:
                return True
            if bucket - 1 in buckets and abs(nums[i] - buckets[bucket - 1]) < w:
                return True
            if bucket + 1 in buckets and abs(nums[i] - buckets[bucket + 1]) < w:
                return True

            buckets[bucket] = nums[i]

            if i >= k:
                del buckets[nums[i - k] // w]

        return False


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], k: int, t: int) -> bool:
        if t < 0:
            return False

        buckets = {}
        for i, val in enumerate(nums):
            bucket = val // t
            for idx in range(bucket - 1, bucket + 1 + 1):
                if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
                    return True

            buckets[bucket] = nums[i]
            if len(buckets) > k:
                del buckets[nums[i - k] // t]

        return False


## self-balancing binary search tree
##############################
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def height(self, node):
        if node:
            return node.height
        return 0

    def set_height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def rotate_right(self, node):
        root = node.left
        node.left = node.left.right
        root.right = node
        node.height = self.set_height(node)
        root.height = self.set_height(root)
        return root

    def rotate_left(self, node):
        root = node.right
        node.right = node.right.left
        root.left = node
        node.height = self.set_height(node)
        root.height = self.set_height(root)
        return root

    def balance(self, node):
        balance = self.height(node.left) - self.height(node.right)

        if balance > 1:
            if self.height(node.left.left) > self.height(node.left.right):
                node = self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                node = self.rotate_right(node)
        elif balance < -1:
            if self.height(node.right.right) > self.height(node.right.left):
                node = self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                node = self.rotate_left(node)
        else:
            node.height = self.set_height(node)

    def insert(self, node, val):
        if node == self.root:
            self.size += 1
        if not node:
            return TreeNode(val)
        if node.val < val:
            node.right = self.insert(node.right, val)
        else:
            node.left = self.insert(node.left, val)

        self.balance(node)

        return node

    def get_min_node(self, node):
        if not node or not node.left:
            return
        return self.get_min_node(node.left)

    def remove(self, node, val):
        if not node:
            return
        if node.val < val:
            node.right = self.remove(node.right, val)
        elif node.val > val:
            node.left = self.remove(node.left, val)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                right_min = self.get_min_node(node.right)
                node.val = right_min.val
                node.right = self.remove(node.right, right_min.val)

        node.height = self.set_height(node)
        self.balance(node)

        return node

    def predecessor(self, node, val):
        if not node:
            return
        if node.val == val:
            return val
        elif node.val > val:
            return self.predecessor(node.left, val)
        else:
            right = self.predecessor(node.right, val)

        return right if right else node.val

    def successor(self, node, val):
        if not node:
            return
        if node.val == val:
            return val
        elif node.val < val:
            return self.successor(node.right, val)
        else:
            left = self.successor(node.left, val)

        return left if left else node.val


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], k: int, t: int) -> bool:
        tree = AVLTree()
        root = tree.root

        for i, num in enumerate(nums):
            predecessor = tree.predecessor(root, num)
            if predecessor and abs(predecessor - num) <= t:
                return True

            successor = tree.successor(root, num)
            if successor and abs(successor - num) <= t:
                return True

            root = tree.insert(root, num)
            if tree.size > k:
                root = tree.remove(root, nums[i - k])

        return False


## naive solution (TLE)
##############################
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], k: int, t: int) -> bool:
        for i in range(len(nums)):
            for j in range(max(i - k, 0), i):
                if abs(nums[i] - nums[j]) <= t:
                    return True

        return False


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(
            Solution().containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0), True
        ),
        self.assertEqual(
            Solution().containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2), True
        ),
        self.assertEqual(
            Solution().containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3), False
        ),


if __name__ == "__main__":
    unittest.main()
