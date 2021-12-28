##
#### Level 3: Problem 2
########################################

# Fuel Injection Perfection
# =========================

# Commander Lambda has asked for your help to refine the automatic quantum
# antimatter fuel injection system for the LAMBCHOP doomsday device. It's a
# great chance for you to get a closer look at the LAMBCHOP -- and maybe sneak
# in a bit of sabotage while you're at it -- so you took the job gladly. 

# Quantum antimatter fuel comes in small pellets, which is convenient since the
# many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a
# time. However, minions dump pellets in bulk into the fuel intake. You need to
# figure out the most efficient way to sort and shift the pellets down to a
# single pellet at a time. 

# The fuel control mechanisms have three operations: 

# 1) Add one fuel pellet
# 2) Remove one fuel pellet
# 3) Divide the entire group of fuel pellets by 2 (due to the destructive
#    energy released when a quantum antimatter pellet is cut in half, the
#    safety controls will only allow this to happen if there is an even number
#    of pellets)

# Write a function called solution(n) which takes a positive integer as a
# string and returns the minimum number of operations needed to transform the
# number of pellets to 1. The fuel intake control panel can only display a
# number up to 309 digits long, so there won't ever be more pellets than you
# can express in that many digits.

# For example:
# solution(4) returns 2: 4 -> 2 -> 1
# solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1
# Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time. 

# The fuel control mechanisms have three operations: 

# 1) Add one fuel pellet
# 2) Remove one fuel pellet
# 3) Divide the entire group of fuel pellets by 2 (due to the destructive
#    energy released when a quantum antimatter pellet is cut in half, the
#    safety controls will only allow this to happen if there is an even number
#    of pellets)

# Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

# For example:
# solution(4) returns 2: 4 -> 2 -> 1
# solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

# Languages
# =========

# To provide a Python solution, edit solution.py
# To provide a Java solution, edit Solution.java

# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.

# -- Python cases --
# Input:
# solution.solution('15')
# Output: 5
# 
# Input:
# solution.solution('4')
# Output: 2
# 
# -- Java cases --
# Input:
# Solution.solution('4')
# Output: 2
# 
# Input:
# Solution.solution('15')
# Output: 5

################################################################################


## Submitted Solution
##############################
def solution(n):
    n = int(n)
    res = 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        elif n == 3 or n + 1 & n > n - 1 & n - 2:
            n -= 1
        else:
            n += 1

        res += 1

    return res


## 
##############################
def solution(n):
    pass


## https://stackoverflow.com/questions/68429960/google-foobar-fuel-injection-perfection
##############################
def solution(n):
    n = int(n)

    if n <= 2:
        return n - 1
    if n % 2 == 0:
        return solution(n // 2) + 1

    return min(solution(n + 1), solution(n - 1)) + 1


## https://www.youtube.com/watch?v=LFax68Dbuvo
##############################
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def solution(n):
    root = TreeNode(int(n))
    queue = [root]
    depth = 0
    seen = set()
    while queue:
        next_queue = []
        for node in queue:
            if node.val in seen:
                continue
            seen.add(node.val)
            if node.val == 1:
                return depth
            if node.val % 2 == 0:
                node.add_child(TreeNode(node.val // 2))
            else:
                node.add_child(TreeNode(node.val - 1))
                node.add_child(TreeNode(node.val + 1))
            for child in node.children:
                next_queue.append(child)
        queue = next_queue
        depth += 1


## my version of above
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


def solution(n):
    root = TreeNode(int(n))
    seen = set()
    queue = [root]
    depth = 0

    while queue:
        next_queue = []
        for node in queue:
            if node.val in seen:
                continue
            seen.add(node.val)

            if node.val == 1:
                return depth

            if node.val % 2 == 0:
                node.children.append(TreeNode(node.val // 2))
            else:
                node.children.append(TreeNode(node.val - 1))
                node.children.append(TreeNode(node.val + 1))

            if node.children:
                queue = node.children

        depth += 1


## https://govanify.com/post/foobar/
##############################
def solution(n):
    n = int(n)
    res = 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        elif n == 3 or n + 1 & n > n - 1 & n - 2:
            n -= 1
        else:
            n += 1

        res += 1

    return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(solution('15'), 5)
        self.assertEqual(solution('4'), 2)


if __name__ == "__main__":
    unittest.main()


