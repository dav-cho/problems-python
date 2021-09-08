##
#### Fizz Buzz (7 kyu)
##########################

def fizzbuzz(n):
    res = []
    hash = {3: 'Fizz', 5: 'Buzz'}
    
    for num in range(1, n + 1):
        curr = ''
        
        for key in hash.keys():
            if num % key == 0:
                curr += hash[key]
            
        if not curr:
            curr = num
            
        res.append(curr)
        
    return res


def fizzbuzz(n):
    res = []
    for num in range(1, n + 1):
        div_3 = num % 3 == 0
        div_5 = num % 5 == 0
        curr = ''
        
        if div_3:
            curr += 'Fizz'
        if div_5:
            curr += 'Buzz'
        if not curr:
            curr = num
        
        res.append(curr)
    
    return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual((), )
        self.assertAlmostEqual((), )


if __name__ == '__main__':
    unittest.main()

