##
#### Count Prims (medium)
########################################

# Given an integer n, return the number of prime numbers that are strictly
# less than n.

# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# Example 2:
# Input: n = 0
# Output: 0

# Example 3:
# Input: n = 1
# Output: 0
 
# Constraints:
# 0 <= n <= 5 * 106

################################################################################

import math


## best* - using array
##############################
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        
        nums = [1] * n
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if nums[i]:
                for multiple in range(i * i, n, i):
                    nums[multiple] = 0
                    
        return nums.count(1) - 2;


## sieve
##############################
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        nums = set()
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if i not in nums:
                for multiple in range(i * i, n, i):
                    nums.add(multiple)
                    
        return n - 2 - len(nums)


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        nums = {}
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if i not in nums:
                for multiple in range(i * i, n, i):
                    nums[multiple] = None   # any arbitrary value
                    
        return n - 2 - len(nums)


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        nums = {}
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if i not in nums:
                for multiple in range(i * i, n, i):
                    nums[multiple] = 1
                    
        return n - 2 - len(nums)


## not optimized [TLE]
##############################
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        nums = [None, None] + list(range(2, n))
        
        for i in range(2, int(math.sqrt(n)) + 1):
            for multiple in range(i * i, n, i):
                nums[multiple] = None
                
        nums = list(filter(lambda x: x, nums))
        
        return len(nums)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().countPrimes(10), 4)
        self.assertEqual(Solution().countPrimes(0), 0)
        self.assertEqual(Solution().countPrimes(1), 0)


if __name__ == "__main__":
    unittest.main()


## LeetCode Solutions
#########################

# Instead of checking if each number is prime or not, what if we mark the
# multiples of a prime number as non-prime?

# We have a nested-loop structure.Now the question is: What are the bounds on
# these two loops? The outer loop will start at 2 and go up to sqrt(n). This is
# because by that point we will have considered all of the possible multiples
# of all the prime numbers below n.

# Now that the outer loop's boundaries are defined, let's define the boundaries
# of the inner loop. We will invariantly pick the next available prime number
# (a number/index not yet marked in the array as a composite) before entering
# the inner loop. Say the index we picked from the outer loop is i, then the
# inner loop will start at i*i and increase by increments of i until it
# surpasses n. In short, we iterate over every multiple of i between i and n.

# The question now is why should we start at i*i. Why not start at 2*i to keep
# things simple? The reason is that all of the previous multiples would already
# have been covered by previous primes. In number theory, the fundamental
# theorem of arithmetic, also called the unique factorization theorem or the
# unique prime factorization theorem, states that every integer greater than 1
# either is a prime number itself or can be represented as the product of prime
# numbers. So the prime numbers smaller than i would have already covered the
# multiples smaller than i*i.


## Approach 1: Sieve of Eratosthenes
########################################
# Time:O(sqrt(n)loglogn))
# - The overall time complexity is O(sqrt(n)loglogn)). The sqrt(n) comes from
#   the outer loop. Each time we hit a prime, we "cross out" the multiples of
#   that prime because we know they aren't prime. But how many iterations do we
#   perform for each prime number? That depends on how many multiples of that
#   number are lower than n. Let's look at a rough estimate of these values for
#   all the primes.
#       - For 2, we have to cross out n/2 numbers.
#       - For 3, we have to cross out n/3 numbers.
#       - For 5, we have to cross out n/5 numbers.
#       - ...etc for each prime less than n.
# - This means that the time complexity of "crossing out" is
#   O(n/2 + n/3 + n/5 + ... + n/(last prime < n). This is bounded by O(loglogn)
#   and the proof is available here. Cheers to this discussion post for
#   explaining the complexity analysis in a detailed manner!

# Space: O(n)
# - Because we use an array of length n+1 to track primes and their multiples.
#   If you use a dictionary instead of an array, you will still end up marking
#   at least n/2 elements as composites of the number 2. Thus, the overall
#   complexity when using a dictionary is also O(n).

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        numbers = {}
        for p in range(2, int(sqrt(n)) + 1):
            if p not in numbers:
                for multiple in range(p*p, n, p):
                    numbers[multiple] = 1
        
        # Exclude "1" and the number "n" itself.
        return n - len(numbers) - 2


