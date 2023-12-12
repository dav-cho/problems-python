##
#### 489. Robot Room Cleaner (hard)
#######################################


## This is the robot's control interface.
## You should not implement it, or speculate about its implementation

#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


##
##############################
class Solution:
    def cleanRoom(self, robot):
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        def backtrack(cell=(0, 0), direction=0):
            seen.add(cell)
            robot.clean()

            for i in range(4):
                new_direction = (direction + i) % 4
                new_cell = (cell[0] + directions[new_direction][0],
                    cell[1] + directions[new_direction][1])
                
                if new_cell not in seen and robot.move():
                    backtrack(new_cell, new_direction)
                    go_back()
                    
                robot.turnRight()
        
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        seen = set()
        backtrack()


## Tests
#############

import unittest


class Test(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        self.assertEqual(solution. , )


if __name__ == "__main__":
    unittest.main()

