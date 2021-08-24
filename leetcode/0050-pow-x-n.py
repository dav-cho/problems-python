##
#### Pow(x, n) (medium)
###########################

# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

# Example 1:
# Input: x = 2.00000, n = 10
# Output: 1024.00000

# Example 2:
# Input: x = 2.10000, n = 3
# Output: 9.26100

# Example 3:
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

# Constraints:

# -100.0 < x < 100.0
# -231 <= n <= 231-1
# -104 <= xn <= 104

################################################################################

## 
##############################
class Solution:
    def myPow(self, x: float, n: int) -> float:
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

## Approach 1: Brute Force
##############################
# Time: O(n) - We will multiply x for n times.
# Space: O(1) - We only need one variable to store the final product of x.

## C++
#class Solution {
#public:
#    double myPow(double x, int n) {
#        long long N = n;
#        if (N < 0) {
#            x = 1 / x;
#            N = -N;
#        }
#        double ans = 1;
#        for (long long i = 0; i < N; i++)
#            ans = ans * x;
#        return ans;
#    }
#};

## Java
#class Solution {
#    public double myPow(double x, int n) {
#        long N = n;
#        if (N < 0) {
#            x = 1 / x;
#            N = -N;
#        }
#        double ans = 1;
#        for (long i = 0; i < N; i++)
#            ans = ans * x;
#        return ans;
#    }
#};

## Approach 2: Fast Power Algorithm Recursive
#################################################
# Time: O(logn) - Each time we apply the formula (x^n)^2 = x^(2*n), n is reduced
#                 by half. Thus we need at most O(logn) computations to get the
#                 result.
# Space: O(logn) - For each computation, we need to store the result of x^(n/2).
#                  We need to do the computation for O(logn) times, so the space
#                  complexity is O(logn)

## C++
#class Solution {
#public:
#    double fastPow(double x, long long n) {
#        if (n == 0) {
#            return 1.0;
#        }
#        double half = fastPow(x, n / 2);
#        if (n % 2 == 0) {
#            return half * half;
#        } else {
#            return half * half * x;
#        }
#    }
#    double myPow(double x, int n) {
#        long long N = n;
#        if (N < 0) {
#            x = 1 / x;
#            N = -N;
#        }
#        return fastPow(x, N);
#    }
#};

## Java
#class Solution {
#    private double fastPow(double x, long n) {
#        if (n == 0) {
#            return 1.0;
#        }
#        double half = fastPow(x, n / 2);
#        if (n % 2 == 0) {
#            return half * half;
#        } else {
#            return half * half * x;
#        }
#    }
#    public double myPow(double x, int n) {
#        long N = n;
#        if (N < 0) {
#            x = 1 / x;
#            N = -N;
#        }
#
#        return fastPow(x, N);
#    }
#};


## Approach 3: Fast Power Algorithm Iterative
#################################################
# Time: O(logn) - For each bit of n 's binary representation, we will at most
#                 multiply once. So the total time complexity is O(logn).
# Space: O(1) - We only need two variables for the current product and the final
#               result of x.

## C++
#class Solution {
#public:
#    double myPow(double x, int n) {
#        long long N = n;
#        if (N < 0) {
#            x = 1 / x;
#            N = -N;
#        }
#        double ans = 1;
#        double current_product = x;
#        for (long long i = N; i ; i /= 2) {
#            if ((i % 2) == 1) {
#                ans = ans * current_product;
#            }
#            current_product = current_product * current_product;
#        }
#        return ans;
#    }
#};

## Java
#class Solution {
#    public double myPow(double x, int n) {
#        long N = n;
#        if (N < 0) {
#            x = 1 / x;
#            N = -N;
#        }
#        double ans = 1;
#        double current_product = x;
#        for (long i = N; i > 0; i /= 2) {
#            if ((i % 2) == 1) {
#                ans = ans * current_product;
#            }
#            current_product = current_product * current_product;
#        }
#        return ans;
#    }
#};

