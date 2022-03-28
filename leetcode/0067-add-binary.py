##
#### 67. Add Binary (easy)
########################################


## built-in methods
##############################
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


##
##############################
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            return self.addBinary(b, a)

        N = len(a)
        b = b.zfill(N)
        res = 0
        for i in range(N - 1, -1, -1):
            res = (res << 1) + (a[i] + b[i])


## bit by bit
##############################
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        N = max(len(a), len(b))
        a, b = a.zfill(N), b.zfill(N)

        carry = 0
        res = []
        for i in range(N - 1, -1, -1):
            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1

            if carry % 2:
                res.append("1")
            else:
                res.append("0")

            carry //= 2

        if carry:
            res.append("1")

        return "".join(reversed(res))


## bit manipulation
##############################
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = map(lambda x: int(x, 2), (a, b))
        while y:
            res = x ^ y
            carry = (x & y) << 1
            x, y = res, carry

        return bin(x)[2:]


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(Solution().addBinary("11", "1"), "100")
        self.assertEqual(Solution().addBinary("1010", "1011"), "10101")


if __name__ == "__main__":
    unittest.main()
