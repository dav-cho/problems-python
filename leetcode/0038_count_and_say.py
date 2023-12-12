##
#### 38. Count and Say (medium)
########################################


## first attempt
##############################
class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"

        for _ in range(n - 1):
            char = res[0]
            count = 1
            curr = ""

            for i in range(1, len(res)):
                if res[i] == char:
                    count += 1
                else:
                    curr += str(count) + char
                    char = res[i]
                    count = 1

            res = curr + str(count) + char

        return res


class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"

        for _ in range(n - 1):
            char = res[0]
            count = 1
            curr = ""

            for i in range(1, len(res)):
                if res[i] == char:
                    count += 1
                else:
                    curr += str(count) + char
                    char = res[i]
                    count = 1

            res = curr + str(count) + char

        return res


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.countAndSay(1), "1")
        self.assertEqual(solution.countAndSay(4), "1211")
        self.assertEqual(solution.countAndSay(5), "111221")


if __name__ == "__main__":
    unittest.main()
