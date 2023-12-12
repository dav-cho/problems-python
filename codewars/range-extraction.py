##
#### Range Extraction (4 kyu)
##################################################


def solution(args):
    res = []
    start = end = args[0]
    
    for num in args[1:] + ['']:
        if num != end + 1:
            if end == start:
                res.append(str(start))
            elif end == start + 1:
                res.extend([str(start), str(end)])
            else:
                res.append(f'{str(start)}-{str(end)}')
                
            start = num
            
        end = num
        
    return ','.join(res)



## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
        self.assertEqual(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')


if __name__ == '__main__':
    unittest.main()


