class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        maxi = 2**33-1
        print(bin(maxi))
        print(bin(n))
        print(bin(n^maxi))
        return int(bin(n^maxi)[2:][::-1][:-1],2)^(2**32-1)
