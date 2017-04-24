import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # if s:
        a = re.subn(r'\W*',"",s)
        l = a[0].lower()
        if l[::-1] == l:
            return True

        else:
            return False



print(Solution().isPalindrome(""))