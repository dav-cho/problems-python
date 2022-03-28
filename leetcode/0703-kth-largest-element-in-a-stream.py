##
#### 703. Kth Largest Element in a Stream (easy)
####################################################


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
        # self.assertCountEqual()
        self.assertEqual(
            Solution.KthLargest(
                ["KthLargest", "add", "add", "add", "add", "add"],
                [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]],
            ),
            [null, 4, 5, 5, 8, 8],
        )


if __name__ == "__main__":
    unittest.main()
