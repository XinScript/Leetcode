class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n

        before = 1
        now = 2
        result = 0
        for i in range(3,n+1):
            result = before+now
            before = now
            now = result
        return result

