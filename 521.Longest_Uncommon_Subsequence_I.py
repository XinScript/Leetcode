class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        la = len(a)
        lb = len(b)
        return -1 if a == b else max(la,lb)
            
        
        