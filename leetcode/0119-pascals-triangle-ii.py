##
#### Pascal's Triangle II
#######################################

# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the
# Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
 
# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]

# Example 2:
# Input: rowIndex = 0
# Output: [1]

# Example 3:
# Input: rowIndex = 1
# Output: [1,1]
 
# Constraints:
# 0 <= rowIndex <= 33
 
# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

################################################################################

## 
##############################
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pass


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

## Approach 1: Brute Force Recursion
########################################
# Time: O(2^k)
# The time complexity recurrence is straightforward:
# T(k,i)=T(k−1,i)+T(k−1,i−1)+O(1)∋T(k,k)=T(k,0)=O(1)
# Thus, T(k, m) takes {k \choose m}(m k) units of constant time. For the kth
# row, total time required is:
# T(k, 0) + T(k, 1) + ... + T(k, k-1) + T(k, k)
# \\ \begin{aligned} &= \sum_{m=0}^k T(k, m) \\ &\simeq \sum_{m=0}^k O({k \choose m}) \\ &\simeq O(\sum_{m=0}^k {k \choose m}) \\ &= O(2^k) \end{aligned}T(k,0)+T(k,1)+...+T(k,k−1)+T(k,k) ​ = m=0 ∑ k ​ T(k,m) ≃ m=0 ∑ k ​ O(( m k ​)) ≃O( m=0 ∑ k ​ ( m k ​)) =O(2 k) ​

# Space: O(k)+O(k)≃O(k)
# We need O(k) space to store the output of the kth row.
# At worst, the recursive call stack has a maximum of k calls in memory, each
# call taking constant space. That's O(k) worst case recursive call stack space.

## Java
#class Solution {
#  private int getNum(int row, int col) {
#    if (row == 0 || col == 0 || row == col) {
#      return 1;
#    }
#
#    return getNum(row - 1, col - 1) + getNum(row - 1, col);
#  }
#
#  public List<Integer> getRow(int rowIndex) {
#    List<Integer> ans = new ArrayList<>();
#
#    for (int i = 0; i <= rowIndex; i++) {
#      ans.add(getNum(rowIndex, i));
#    }
#
#    return ans;
#  }
#}


## Approach 2: Dynamic Programming
###################
# Time: O(k^2)
# - Simple memoization would make sure that a particular element in a row is only
#   calculated once. Assuming that our memoization cache allows constant time lookup and updation (like a hash-map), it takes constant time to calculate each element in Pascal's triangle.
# - Since calculating a row requires calculating all the previous rows as well,
#   we end up calculating 1+2+3+...+(k+1)= 2 (k+1)(k+2)≃k^2 elements for the
#   kth row.

# Space: O(k)+O(k)≃O(k).
# - Simple memoization would need to hold all 1+2+3+...+(k+1)= 2 ((k+1)(k+2)) / 2
#   elements in the worst case. That would require O(k^2) space.
# - Saving space by keeping only the latest generated row, we need only O(k)
#   extra space, other than the O(k) space required to store the output.

## Java
#class Solution {
#  public List<Integer> getRow(int rowIndex) {
#    List<Integer> curr,
#        prev =
#            new ArrayList<>() {
#              {
#                add(1);
#              }
#            };
#
#    for (int i = 1; i <= rowIndex; i++) {
#      curr =
#          new ArrayList<>(i + 1) {
#            {
#              add(1);
#            }
#          };
#
#      for (int j = 1; j < i; j++) {
#        curr.add(prev.get(j - 1) + prev.get(j));
#      }
#
#      curr.add(1);
#
#      prev = curr;
#    }
#
#    return prev;
#  }
#}


## Approach 3: Memory-efficient Dynamic Programming
#######################################################
# Time: O(k^2)
# Same as the previous dynamic programming approach.

# Space: O(k)
# No extra space is used other than that required to hold the output.
# Although there is no savings in theoretical computational complexity, in
# practice there are some minor wins:
# - We have one vector/array instead of two. So memory consumption is roughly
#   half.
# - No time wasted in swapping references to vectors for previous and current
#   row.
# - Locality of reference shines through here. Since every read is for
#   consecutive memory locations in the array/vector, we get a performance
#   boost.

## Java
#class Solution {
#  public List<Integer> getRow(int rowIndex) {
#    List<Integer> row =
#        new ArrayList<>(rowIndex + 1) {
#          {
#            add(1);
#          }
#        };
#
#    for (int i = 0; i < rowIndex; i++) {
#      for (int j = i; j > 0; j--) {
#        row.set(j, row.get(j) + row.get(j - 1));
#      }
#      row.add(1);
#    }
#
#    return row;
#  }
#}


## Approach 4: Math! (specifically, Combinatorics)
######################################################
# Time: O(k) - Each term is calculated once, in constant time.
# Space: O(k) - No extra space required other than that required to hold the
#               output.

## Java
#class Solution {
#  public List<Integer> getRow(int n) {
#    List<Integer> row =
#        new ArrayList<>() {
#          {
#            add(1);
#          }
#        };
#
#    for (int k = 1; k <= n; k++) {
#      row.add((int) ((row.get(row.size() - 1) * (long) (n - k + 1)) / k));
#    }
#
#    return row;
#  }
#}
