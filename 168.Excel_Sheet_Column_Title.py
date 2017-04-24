class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ""
        while n!=0:
            d = (n-1)%26
            s=chr(65+d)+s
            n=int((n-1)/26)

        return s


print(Solution().convertToTitle(28))
