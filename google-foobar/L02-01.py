##
#### Level 2: Problem 1
########################################

# Hey, I Already Did That!
# ========================

# Commander Lambda uses an automated algorithm to assign minions randomly to
# tasks, in order to keep minions on their toes. But you've noticed a flaw in
# the algorithm -- it eventually loops back on itself, so that instead of
# assigning new minions as it iterates, it gets stuck in a cycle of values so
# that the same minions end up doing the same tasks over and over again. You
# think proving this to Commander Lambda will help you make a case for your
# next promotion. 

# You have worked out that the algorithm has the following process: 

# 1. Start with a random minion ID n, which is a nonnegative integer of length
#    k in base b
# 2. Define x and y as integers of length k.  x has the digits of n in
#    descending order, and y has the digits of n in ascending order
# 3. Define z = x - y.  Add leading zeros to z to maintain length k if
#    necessary
# 4. Assign n = z to get the next minion ID, and go back to step 2

# For example, given minion ID n = 1211, k = 4, b = 10, then x = 2111, y = 1112
# and z = 2111 - 1112 = 0999. Then the next minion ID will be n = 0999 and the
# algorithm iterates again: x = 9990, y = 0999 and z = 9990 - 0999 = 8991, and
# so on.

# Depending on the values of n, k (derived from n), and b, at some point the
# algorithm reaches a cycle, such as by reaching a constant value. For example,
# starting with n = 210022, k = 6, b = 3, the algorithm will reach the cycle of
# values [210111, 122221, 102212] and it will stay in this cycle no matter how
# many times it continues iterating. Starting with n = 1211, the routine will
# reach the integer 6174, and since 7641 - 1467 is 6174, it will stay as that
# value no matter how many times it iterates.

# Given a minion ID as a string n representing a nonnegative integer of length
# k in base b, where 2 <= k <= 9 and 2 <= b <= 10, write a function
# solution(n, b) which returns the length of the ending cycle of the algorithm
# above starting with n. For instance, in the example above, solution(210022, 3)
# would return 3, since iterating on 102212 would return to 210111 when done in
# base 3. If the algorithm reaches a constant, such as 0, then the length is 1.

# Languages
# =========

# To provide a Java solution, edit Solution.java
# To provide a Python solution, edit solution.py

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Java cases --
# Input:
# Solution.solution('210022', 3)
# Output: 3

# Input:
# Solution.solution('1211', 10)
# Output: 1

# -- Python cases --
# Input:
# solution.solution('1211', 10)
# Output: 1

# Input:
# solution.solution('210022', 3)
# Output: 3

################################################################################


## Submitted Solution
##############################
def solution(n, b):
    def convert_base(n, b):
        digits = []
        while n:
            n, digit = divmod(int(n), b)
            digits.append(str(digit))
        return ''.join(digits[::-1])

    def to_base10(n, b):
        pow = 0
        res = 0
        for i in range(k -1, -1, -1):
            digit = int(n[i]) * b ** pow
            res += digit
            pow += 1
        return res

    def calc_z(n):
        x = ''.join(sorted(n, reverse=True))
        y = ''.join(sorted(n))
        int_x = int(to_base10(x, b))
        int_y = int(to_base10(y, b))
        int_z = int_x - int_y
        z = convert_base(int_z, b).zfill(k)
        return z
    
    k = len(n)
    ids = []
    seen = set()
    while n not in seen:
        ids.append(n)
        seen.add(n)
        z = calc_z(n)
        n = z

    idx = -1
    while z != ids[idx]:
        idx -= 1

    cycle = ids[idx:]
    return len(cycle)


## 
##############################
def solution(n, b):
    pass


## attempt 1
##############################

def solution(n, b):
    def calc_z(n):
        k = len(n)
        x = ''.join(sorted(n, reverse=True))
        y = ''.join(sorted(n))
        z = str(int(x, b) - int(y, b)).zfill(k)

        return z

    ids = []
    seen = set()
    idx = 1
    while n not in seen:
        ids.append(n)
        seen.add(n)
        print('ids', ids)
        print('seen', seen)
        z = calc_z(n)
        if z in seen:
            curr = [z]
            while curr == ids[-idx:]:
                print('res ids', ids[-idx:])
                print('res curr', curr)
                idx += 1
                z = calc_z(z)
                print('res z', z)
                curr.append(z)
            print('after res curr', curr)
            print('afer res ids', ids[-idx + 1:])
        n = z

    print('--------------------')
    print('ans', len(curr) - 1)
    return len(curr) - 1


## attempt 2
##############################

def solution(n, b):
    def calc_z(n):
        k = len(n)
        print('n before:', n)
        n = str(int(n, b))
        print('n integer base 10:', n)
        x = ''.join(sorted(n, reverse=True))
        y = ''.join(sorted(n))
        int_x = int(x, b)
        int_y = int(y, b)
        z = str(int_x - int_y).zfill(k)
        #z = str(int(x, b) - int(y, b)).zfill(k)
        print('int x', int(x, b))

        #print('n:', n)
        #print('k:', k)
        #print('x:', x)
        #print('y:', y)
        print('int x', int_x)
        print('int y', int_y)
        print('z:', z)

        return z

    ids = []
    num = n
    for _ in range(10):
        print(_)
        ids.append(num)
        z = calc_z(num)
        print('------------------------------')
        print('num', num)
        print('z', z)
        print('ids:', ids)
        num = z


## attempt 3
##############################

# Depending on the values of n, k (derived from n), and b, at some point the
# algorithm reaches a cycle, such as by reaching a constant value. For example,
# starting with n = 210022, k = 6, b = 3, the algorithm will reach the cycle of
# values [210111, 122221, 102212] and it will stay in this cycle no matter how
# many times it continues iterating.

# n = 210022, k = 6, b = 3
# [210111, 122221, 102212]

def solution(n, b):
    def convert(n, b):
        digits = []
        while n:
            n, digit = divmod(int(n), b)
            digits.append(str(digit))

        return int(''.join(digits[::-1]))

    def calc_z(n):
        k = len(n)
        int_n = convert(n, b)
        print('n', n)
        print('int_n', int_n)
        print('')

        x = ''.join(sorted(n, reverse=True))
        int_x = convert(x, b)
        print('\nx', x)
        print('int_x', int_x)

        y = ''.join(sorted(n))
        int_y = convert(y, b)
        print('\nint_y', int_y)
        print('y', y)

        int_z = int_x - int_y
        z = convert(int_z, b)
        print('\nz', z)
        print('int_z', int_z)

        return z

    ids = []
    seen = set()
    count = 0
    while n not in seen:
        print('------------------------------')
        count += 1
        ids.append(n)
        seen.add(n)
        z = calc_z(n)
        n = z
        print(ids)
        print(seen)


## attempt 4
##############################
def solution(n, b):
    def convert_base(n, b):
        digits = []
        while n:
            n, digit = divmod(int(n), b)
            digits.append(str(digit))

        return ''.join(digits[::-1])

    def to_base10(n, b):
        pow = 0
        res = 0
        for i in range(k -1, -1, -1):
            digit = int(n[i]) * b ** pow
            res += digit
            pow += 1

        return res

    def calc_z(n):
        x = ''.join(sorted(n, reverse=True))
        y = ''.join(sorted(n))

        int_x = int(to_base10(x, b))
        int_y = int(to_base10(y, b))

        int_z = int_x - int_y
        z = convert_base(int_z, b)
        #print('x:', x)
        #print('y:', y)
        #print('z:', z)
        #print('int_x:', int_x)
        #print('int_y:', int_y)
        #print('int_z:', int_z)

        return z
    
    k = len(n)

    ids = []
    seen = set()
    while n not in seen:
        ids.append(n)
        seen.add(n)
        z = calc_z(n)
        n = z

    print('z:', z)
    print('ids:', ids)
    print('seen:', seen)

    idx = -1
    while z != ids[idx]:
        idx -= 1

    cycle = ids[idx:]
    print(cycle)

    return len(cycle)


## attempt 5
##############################
def solution(n, b):
    def convert_base(n, b):
        digits = []
        while n:
            n, digit = divmod(int(n), b)
            digits.append(str(digit))
        return ''.join(digits[::-1])

    def to_base10(n, b):
        pow = 0
        res = 0
        for i in range(k -1, -1, -1):
            digit = int(n[i]) * b ** pow
            res += digit
            pow += 1
        return res

    def calc_z(n):
        x = ''.join(sorted(n, reverse=True))
        y = ''.join(sorted(n))
        int_x = int(to_base10(x, b))
        int_y = int(to_base10(y, b))
        int_z = int_x - int_y
        z = convert_base(int_z, b).zfill(k)
        return z
    
    k = len(n)
    ids = []
    seen = set()
    while n not in seen:
        ids.append(n)
        seen.add(n)
        z = calc_z(n)
        n = z

    idx = -1
    while z != ids[idx]:
        idx -= 1

    cycle = ids[idx:]
    return len(cycle)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        #self.assertEqual(solution('102212', 3), 3)
        #self.assertEqual(solution('210022', 3), 3)

        # -- Python cases --
        self.assertEqual(solution('1211', 10), 1)
        self.assertEqual(solution('210022', 3), 3)

        # -- Java cases --
        #self.assertEqual(solution('1211', 10), 1)
        #self.assertEqual(solution('210022', 3), 3)



if __name__ == "__main__":
    unittest.main()


