##
#### 328. Odd Even Linked List (medium)
###########################################


from typing import Optional

## Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


##
##############################
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        even = head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().oddEvenList([1, 2, 3, 4, 5]), [1, 3, 5, 2, 4])
        self.assertEqual(
            Solution().oddEvenList([2, 1, 3, 5, 6, 4, 7]), [2, 3, 6, 7, 1, 5, 4]
        )


if __name__ == "__main__":
    unittest.main()
