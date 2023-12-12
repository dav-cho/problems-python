##
#### 841. Keys and Rooms (medium)
#####################################


## dfs
##############################
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        while stack:
            for key in rooms[stack.pop()]:
                if not seen[key]:
                    seen[key] = True
                    stack.append(key)

        return all(seen)


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        seen, stack = {0}, [0]
        while stack:
            for key in rooms[stack.pop()]:
                if key not in seen:
                    seen.add(key)
                    stack.append(key)

        return len(seen) == len(rooms)


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution.canVisitAllRooms([[1], [2], [3], []]), True)
        self.assertEqual(
            solution.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]), False
        )


if __name__ == "__main__":
    unittest.main()
