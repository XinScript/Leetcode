class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            result = int(str(x)[::-1])
        else:
            result =  -int(str(-x)[::-1])

        if abs(result) > 2**31-1:
            return 0
        return result

