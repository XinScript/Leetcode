class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        mapper = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        def newhex(s):
            return mapper[s] if s<=15 else newhex(s>>4)+mapper[s&15]
        if num > 0:
            return newhex(num)
        elif num < 0:
            return newhex(2**32+num)
        else:
            return '0'
