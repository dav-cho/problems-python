##
#### 384. Shuffle an Array (medium)
########################################


## fisher-yates algorithm
##############################
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        self.nums = list(self.original)
        
        return self.nums

    def shuffle(self) -> List[int]:
        N = len(self.nums)
        
        for i in range(N):
            rand_idx = random.randrange(i, N)
            self.nums[i], self.nums[rand_idx] = self.nums[rand_idx], self.nums[i]
            
        return self.nums


## brute force
##############################
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        self.nums = list(self.original)
        
        return self.nums

    def shuffle(self) -> List[int]:
        nums_copy = list(self.nums)
        
        for i in range(len(self.nums)):
            remove_idx = random.randrange(len(nums_copy))
            self.nums[i] = nums_copy.pop(remove_idx)
            
        return self.nums


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )


if __name__ == "__main__":
    unittest.main()
