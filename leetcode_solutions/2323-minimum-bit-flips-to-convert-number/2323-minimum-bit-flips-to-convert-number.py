class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        n = 0
        start = bin(start).split('b')[1]
        goal = bin(goal).split('b')[1]
        if len(start) != len(goal):
            if len(start) < len(goal):
                diff = len(goal) - len(start)
                start = '0'*diff + start
            elif len(goal) < len(start):
                diff = len(start) - len(goal)
                goal = '0'*diff + goal
        for i in range(len(start)):
            if start[i] != goal[i]:
                n += 1
        return n
