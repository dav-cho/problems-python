##
#### Kth Largest Element in a Stream (easy)
###############################################

# Design a class to find the kth largest element in a stream. Note that it is
# the kth largest element in the sorted order, not the kth distinct element.

# Implement KthLargest class:
# - KthLargest(int k, int[] nums) Initializes the object with the integer k and
#   the stream of integers nums.
# - int add(int val) Appends the integer val to the stream and returns the
#   element representing the kth largest element in the stream.

# Example 1:
# Input:
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output:
# [null, 4, 5, 5, 8, 8]
# Explanation:
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8

# Constraints:
# 1 <= k <= 104
# 0 <= nums.length <= 104
# -104 <= nums[i] <= 104
# -104 <= val <= 104
# At most 104 calls will be made to add.
# It is guaranteed that there will be at least k elements in the array when you search for the kth element.

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

################################################################################


## heap
##############################
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


## 
##############################
class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        pass

    def add(self, val: int) -> int:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        #self.assertCountEqual()
        self.assertEqual(Solution.KthLargest(["KthLargest", "add", "add", "add", "add", "add"], [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]), [null, 4, 5, 5, 8, 8])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Heap
##############################
# Given N as the length of nums and M as the number of calls to add(),

# Time: O(N⋅log(N)+M⋅log(k))
# - The time complexity is split into two parts. First, the constructor needs
#   to turn nums into a heap of size k. In Python, heapq.heapify() can turn
#   nums into a heap in O(N) time. Then, we need to remove from the heap until
#   there are only k elements in it, which means removing N - k elements. Since
#   k can be, say 1, in terms of big O this is N operations, with each operation
#   costing log(N). Therefore, the constructor costs O(N+N⋅log(N))=O(N⋅log(N)).
# - Next, every call to add() involves adding an element to heap and potentially
#   removing an element from heap. Since our heap is of size k, every call to
#   add() at worst costs O(2∗log(k))=O(log(k)). That means M calls to add()
#   costs O(M⋅log(k)).

# Space: O(N)
# - The only extra space we use is the heap. While during add() calls we limit
#   the size of the heap to k, in the constructor we start by converting nums
#   into a heap, which means the heap will initially be of size N.
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


