import re


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return 0
        else:
            new = re.split(r'\s*', s)
            while new:
                a = new.pop()
                if a != "":
                    return len(a)
            return 0

