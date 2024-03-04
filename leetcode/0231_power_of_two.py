"""
231. Power of Two (easy)
"""


class IsolateRightmostBit:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & -n == n


class TurnOffRightmostBit:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
