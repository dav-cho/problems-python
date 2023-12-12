##
#### 509. Fibonacci Number (easy)
#####################################


## recursive
##############################
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        return self.fib(n - 2) + self.fib(n - 1)


## bottom-up tabulation
##############################
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        cache = [0] * (n + 1)
        cache[1] = 1
        for i in range(2, n + 1):
            cache[i] = cache[i - 2] + cache[i - 1]
            
        return cache[n]


## memoized recursive
##############################
class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        
        def recursive_fib(n):
            if n in cache:
                return cache[n]
            
            if n < 2:
                result = n
            else:
                result = recursive_fib(n - 2) + recursive_fib(n - 1)
                
            cache[n] = result
            return result
        
        return recursive_fib(n)


class Solution:
    def __init__(self):
        self.cache = {0: 0, 1: 1}
        
    def fib(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        
        self.cache[n] = self.fib(n - 2) + self.fib(n - 1)
        return self.cache[n]


## iterative bottom-up
##############################
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        a, b, c = 0, 1, 0
        for _ in range(2, n + 1):
            c = a + b
            a, b = b, c
            
        return c


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        a, b, c = 0, 1, 0
        for _ in range(2, n + 1):
            c = a + b
            a = b
            b = c
            
        return c


## TODO: matrix exponentiation
##############################
class Solution:
    def fib(self, n: int) -> int:
        pass


## math
##############################
class Solution:
    def fib(self, n: int) -> int:
        golden_ratio = (1 + (5 ** 0.5)) / 2
        
        return int(round((golden_ratio ** n) / (5 ** 0.5)))


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )


if __name__ == "__main__":
    unittest.main()
