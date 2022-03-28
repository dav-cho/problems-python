##
#### 350. Intersection of Two Arrays II (easy)
##################################################


from collections import Counter


## bit manipulation
##############################
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return (Counter(nums1) & Counter(nums2)).elements()


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        a, b = map(Counter, (nums1, nums2))

        return list((a & b).elements())


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        a, b = map(Counter, (nums1, nums2))
        intersect = a & b
        res = []

        for num in intersect:
            for _ in range(intersect[num]):
                res.append(num)

        return res


## hash map
##############################
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        counts = Counter(nums1)
        k = 0

        for num in nums2:
            if num in counts and counts[num] > 0:
                counts[num] -= 1
                nums1[k] = num
                k += 1

        return nums1[:k]


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        seen = defaultdict(int)

        for num in nums1:
            seen[num] += 1

        k = 0

        for num in nums2:
            if seen[num] > 0:
                nums1[k] = num
                k += 1
                seen[num] -= 1

        return nums1[:k]


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        a = nums1 if len(nums1) > len(nums2) else nums2
        b = nums1 if a == nums2 else nums2

        intersect = []
        counts = Counter(b)

        for num in a:
            if num in counts and counts[num] > 0:
                intersect.append(num)
                counts[num] -= 1

        return intersect


## sort
##############################
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()

        i = j = k = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                nums1[k] = nums1[i]
                i += 1
                j += 1
                k += 1

        return nums1[:k]


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()

        i = j = k = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                nums1[k] = nums2[j]
                i += 1
                j += 1
                k += 1

        return nums1[:k]


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()

        i = j = k = 0

        try:
            while i < len(nums1) and k < len(nums2):
                if nums1[i] > nums2[j]:
                    j += 1
                elif nums1[i] < nums2[j]:
                    i += 1
                else:
                    nums1[k] = nums2[j]
                    i += 1
                    j += 1
                    k += 1
        except IndexError:
            pass

        return nums1[:k]


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.intersect([1, 2, 2, 1], [2, 2]), [2, 2])
        self.assertEqual(solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9])


if __name__ == "__main__":
    unittest.main()
