# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
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

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        """
        Always move in clockwise manner, up -> right -> down -> left. Functions will return in
        the same order
        Intuition -> Go forward, clean the cell and mark that cell. At the obstacle turn right,           again go forward. => Always turn right at the obstacle and go forward. 
        So for given cell, if robot moves forward and hits the dead end then robot will clean that
        dead end square and comes back to the original cell after finishing backTrack() function 
        for that dead end cell via goBack() on line 76.

        """
        directions = [[-1,0],[0,1],[1,0],[0,-1]]        
        visit = set()
        
        def goBack():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        """
        direction variable
        0 -> going up
        1 -> going right
        2 -> going down
        3 -> going left
        """
        def backTrack(x, y, direction):
            visit.add((x,y))
            robot.clean()
            
            for i in xrange(4):
                newDirection = (direction + i) % 4
                newX = x + directions[newDirection][0]
                newY = y + directions[newDirection][1]
                
                if (newX, newY) not in visit and robot.move():
                    backTrack(newX, newY, newDirection)
                    goBack()
                robot.turnRight()
        backTrack(0,0,0)