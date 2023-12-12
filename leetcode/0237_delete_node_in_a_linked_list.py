##
#### 237. Delete Node in a Linked List (easy)
#################################################


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


## first attempt
##############################
class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


class Solution:
    def deleteNode(self, node):
        node.val, node.next = node.next.val, node.next.next


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()


if __name__ == "__main__":
    unittest.main()
