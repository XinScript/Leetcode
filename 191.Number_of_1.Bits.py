class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            r = n%2
            if r == 1:
                count+=1
            n = int(n/2)
        return count
