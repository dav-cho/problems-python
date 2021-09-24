##
#### Intersection of Two Arrays II (easy)
#############################################

# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must appear as many times as it
# shows in both arrays and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

# Follow up:

# - What if the given array is already sorted? How would you optimize your
#   algorithm?
# - What if nums1's size is small compared to nums2's size? Which algorithm is
#   better?
# - What if elements of nums2 are stored on disk, and the memory is limited
#   such that you cannot load all elements into the memory at once?

################################################################################


## bit manipulation
##############################
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        a, b = map(Counter, (nums1, nums2))
        
        return list((a & b).elements())


## sort
##############################
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


## hash map
##############################
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


## attempt 1
##############################
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersect = []
        
        for num in nums1:
            if num in nums2:
                intersect.append(num)
                nums2.remove(num)
                
        return intersect


## attempt 2
##############################
from collections import Counter

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


## attempt 2 optimized
# - make counter with shorter array for space optimization
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        long = nums1 if len(nums1) > len(nums2) else nums2
        short = nums2 if long == nums1 else nums1
        
        counts = Counter(short)
        intersect = []

        for num in long:
            if num in counts and counts[num] > 0:
                intersect.append(num)
                counts[num] -= 1
                
        return intersect


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.intersect([1,2,2,1], [2,2]), [2,2])
        self.assertEqual(solution.intersect([4,9,5], [9,4,9,8,4]), [4,9])


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Hash Map
##############################
# Time: O(n + m) - Where n and m are the lenghts of the arrays. We iterate
#                  through the first, and then through the second array; insert
#                  and lookup operations in the hash map take constant time.
# Space: O(min(n, m)) - We use hash map to store numbers (and their counts)
#                       from the smaller array.

## C++
#vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
#    if (nums1.size() > nums2.size()) {
#        return intersect(nums2, nums1);
#    }
#    unordered_map<int, int> m;
#    for (auto n : nums1) {
#        ++m[n];
#    }
#    int k = 0;
#    for (auto n : nums2) {
#        auto it = m.find(n);
#        if (it != end(m) && --it->second >= 0) {
#            nums1[k++] = n;
#        }
#    }
#    return vector(begin(nums1), begin(nums1) + k);
#}

## Java
#public int[] intersect(int[] nums1, int[] nums2) {
#    if (nums1.length > nums2.length) {
#        return intersect(nums2, nums1);
#    }
#    HashMap<Integer, Integer> m = new HashMap<>();
#    for (int n : nums1) {
#        m.put(n, m.getOrDefault(n, 0) + 1);
#    }
#    int k = 0;
#    for (int n : nums2) {
#        int cnt = m.getOrDefault(n, 0);
#        if (cnt > 0) {
#            nums1[k++] = n;
#            m.put(n, cnt - 1);
#        }
#    }
#    return Arrays.copyOfRange(nums1, 0, k);
#}


## Approach 2: Sort
##############################
# Time: O(nlogn+mlogm)
# - Where n and m are the lengths of the arrays. We sort two arrays
#   independently, and then do a linear scan.
# Space: From O(logn+logm) to O(n+m)
# - Depending on the implementation of the sorting algorithm. For the complexity
#   analysis purposes, we ignore the memory required by inputs and outputs.

## C++
#vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
#    sort(begin(nums1), end(nums1));
#    sort(begin(nums2), end(nums2));
#    int i = 0, j = 0, k = 0;
#    while (i < nums1.size() && j < nums2.size()) {
#        if (nums1[i] < nums2[j]) {
#            ++i;
#        } else if (nums1[i] > nums2[j]) {
#            ++j;
#        } else {
#            nums1[k++] = nums1[i++];
#            ++j;
#        }
#    }
#    return vector<int>(begin(nums1), begin(nums1) + k);
#}

## Java
#public int[] intersect(int[] nums1, int[] nums2) {
#    Arrays.sort(nums1);
#    Arrays.sort(nums2);
#    int i = 0, j = 0, k = 0;
#    while (i < nums1.length && j < nums2.length) {
#        if (nums1[i] < nums2[j]) {
#            ++i;
#        } else if (nums1[i] > nums2[j]) {
#            ++j;
#        } else {
#            nums1[k++] = nums1[i++];
#            ++j;
#        }
#    }
#    return Arrays.copyOfRange(nums1, 0, k);
#}


## Approach 3: Built-in Intersection
########################################
# Time: Same as Approach 2
# Space: Same as Approach 2
#vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
#    sort(begin(nums1), end(nums1));
#    sort(begin(nums2), end(nums2));
#    nums1.erase(set_intersection(begin(nums1), end(nums1),
#        begin(nums2), end(nums2), begin(nums1)), end(nums1));
#    return nums1;
#}


