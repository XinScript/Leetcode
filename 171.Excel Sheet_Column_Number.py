class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        def a(c,i):
            return (ord(c)-65+1)*26**i
        size = len(s)-1
        result = 0
        for i in list(map(a,s)):
            result+=i*(26**size)
            size-=1

        return result

