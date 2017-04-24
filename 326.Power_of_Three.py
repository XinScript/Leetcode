import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        a = round(math.log(n,3),13)
        gap = abs(a-int(a))
        if gap<= 0.00000000000001 or gap >=0.99999999999999 :
            return True
        else:
            return False


print(Solution().isPowerOfThree(243))