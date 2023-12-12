##
#### 279. Perfect Squares (medium)
######################################


## recursive
######################
class Solution:
    def numSquares(self, n: int) -> int:
        pass


## dynamic programming
##########################
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(0, int(n**0.5) + 1)]
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break

                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[-1]


## greedy enumeration
#########################
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = set(i * i for i in range(1, int(n**0.5) + 1))

        def is_divided_by(n, count):
            if count == 1:
                return n in square_nums

            for k in square_nums:
                if is_divided_by(n - k, count - 1):
                    return True
            return False

        for count in range(1, n + 1):
            if is_divided_by(n, count):
                return count


## greedy + bfs
###################
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i * i for i in range(1, int(n**0.5) + 1)]
        level = 0
        queue = {n}
        while queue:
            level += 1
            next_queue = set()
            for remainder in queue:
                for square_num in square_nums:
                    if remainder == square_num:
                        return level
                    elif remainder < square_num:
                        break
                    else:
                        next_queue.add(remainder - square_num)
            queue = next_queue

        return level


## mathematics
##################
class Solution:
    def numSquares(self, n: int) -> int:
        while (n & 3) == 0:
            n >>= 2

        if (n & 7) == 7:
            return 4
        if self.is_square(n):
            return 1

        for i in range(1, int(n**0.5) + 1):
            if self.is_square(n - i * i):
                return 2

        return 3

    def is_square(self, n: int) -> bool:
        root = int(n**0.5)
        return root * root == n
