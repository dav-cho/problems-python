"""
67. Add Binary (easy)
"""


class Builtin1:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


class Builtin2:
    def addBinary(self, a: str, b: str) -> str:
        return f"{int(a, 2) + int(b, 2):b}"


class BitByBit:
    def addBinary(self, a: str, b: str) -> str:
        n = max(map(len, [a, b]))
        a = a.zfill(n)
        b = b.zfill(n)

        res = []
        carry = 0
        for i in range(n - 1, -1, -1):
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
        return "".join(res[::-1])


class BitManipulation:
    def addBinary(self, a: str, b: str) -> str:
        res = int(a, 2)
        carry = int(b, 2)
        while carry:
            res, carry = res ^ carry, (res & carry) << 1
        return bin(res)[2:]


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
