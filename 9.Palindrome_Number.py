import math
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x < 10:
            return True
        elif x%10 == 0:
            return False
        else:
            res = 0
            while x>res:
                res = res*10+x%10
                x//=10

            return x == res or x == res//10