class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False

        if n^(n-1) == 2*n-1:
            return True

        return False


print(16^0)