##
#### 412. Fizz Buzz (easy)
##############################


## hash table
##############################
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        table = { 3: 'Fizz', 5: 'Buzz' }
        
        for i in range(1, n + 1):
            curr = ''
            
            for num in table:
                if not i % num:
                    curr += table[num]
                    
            if not curr:
                curr = str(i)
                
            res.append(curr)
            
        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )


if __name__ == "__main__":
    unittest.main()
