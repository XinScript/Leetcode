class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 2 if n%2==0 else 1
        while n >0:
            n-=i
            i = i<<2
        return True if n == 0 else False
            
                
            
            