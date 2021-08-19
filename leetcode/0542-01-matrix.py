##
#### 01 Matrix (medium)
###########################

# Given an m x n binary matrix mat, return the distance of the nearest 0 for
# each cell.

# The distance between two adjacent cells is 1.

# Example 1:
#  [[0, 0, 0],
#   [0, 1, 0],
#   [0, 0, 0]]
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]

# Example 2:
#  [[0, 0, 0],
#   [0, 1, 0],
#   [1, 1, 1]]
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
 
# Constraints:
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.

################################################################################

## 
##############################
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
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

## Approach 1: Brute force [Time Limit Exceeded]
####################################################
# Time: O((r*c)^2) - Iterating over the entire matrix for each 1 in the matrix.
# Space: O(1) - No extra space is required other than the space used to store
#               the output (dist), and the output does not count towards the
#               space complexity.

## C++
#class Solution {
#public:
#    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
#        int rows = matrix.size();
#        if (rows == 0)
#            return matrix;
#        int cols = matrix[0].size();
#        vector<vector<int>> dist(rows, vector<int> (cols, INT_MAX));
#        for (int i = 0; i < rows; i++) {
#            for (int j = 0; j < cols; j++) {
#                if (matrix[i][j] == 0) {
#                    dist[i][j] = 0;
#                } else {
#                    for (int k = 0; k < rows; k++) {
#                        for (int l = 0; l < cols; l++) {
#                            if (matrix[k][l] == 0) {
#                                int dist_01 = abs(k - i) + abs(l - j);
#                                dist[i][j] = min(dist[i][j], abs(k - i) + abs(l - j));
#                            }
#                        }
#                    }
#                }
#            }
#        }
#        return dist;
#    }
#};


## Approach 2: Using BFS
############################
# Time: O(r * c) - Since, the new cells are added to the queue only if their
#                  current distance is greater than the calculated distance,
#                  cells are not likely to be added multiple times.
# Space: O(r * c) - Space is required to maintain the queue.

## C++
#class Solution {
#public:
#    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
#        int rows = matrix.size();
#        if (rows == 0)
#            return matrix;
#        int cols = matrix[0].size();
#        vector<vector<int>> dist(rows, vector<int> (cols, INT_MAX));
#        queue<pair<int, int>> q;
#        for (int i = 0; i < rows; i++) {
#            for (int j = 0; j < cols; j++) {
#                if (matrix[i][j] == 0) {
#                    dist[i][j] = 0;
#                    q.push({ i, j }); //Put all 0s in the queue.
#                }
#            }
#        }
#
#        int dir[4][2] = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
#        while (!q.empty()) {
#            pair<int, int> curr = q.front();
#            q.pop();
#            for (int i = 0; i < 4; i++) {
#                int new_r = curr.first + dir[i][0], new_c = curr.second + dir[i][1];
#                if (new_r >= 0 && new_c >= 0 && new_r < rows && new_c < cols) {
#                    if (dist[new_r][new_c] > dist[curr.first][curr.second] + 1) {
#                        dist[new_r][new_c] = dist[curr.first][curr.second] + 1;
#                        q.push({ new_r, new_c });
#                    }
#                }
#            }
#        }
#        return dist;
#    }
#};


## Approach 3: Dynamic Programming
######################################
# Time: O(r * c) - We perform two passes over the matrix and each pass requires
#                  O(r⋅c) time.
# Space: O(1) - No extra space is required other than the space used to store
#               the output (dist), and the output does not count towards the
#               space complexity.

## C++
#class Solution {
#public:
#    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
#        int rows = matrix.size();
#        if (rows == 0) 
#            return matrix;
#        int cols = matrix[0].size();
#        vector<vector<int>> dist(rows, vector<int> (cols, INT_MAX - 100000));
#
#        //First pass: check for left and top
#        for (int i = 0; i < rows; i++) {
#            for (int j = 0; j < cols; j++) {
#                if (matrix[i][j] == 0) {
#                    dist[i][j] = 0;
#                } else {
#                    if (i > 0)
#                        dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1);
#                    if (j > 0)
#                        dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1);
#                }
#            }
#        }
#
#        //Second pass: check for bottom and right
#        for (int i = rows - 1; i >= 0; i--) {
#            for (int j = cols - 1; j >= 0; j--) {
#                if (i < rows - 1)
#                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1);
#                if (j < cols - 1)
#                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1);
#            }
#        }
#        return dist;
#    }
#};


