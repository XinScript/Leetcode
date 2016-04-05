class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a = {}
        b = {}
        i = 0
        size = len(s)
        while i < size:
            temp = a.get(s[i])
            temp2 = b.get(t[i])
            if temp and temp2:
                if temp != t[i] or temp2!=s[i]:
                    return False
            elif not temp and not temp2:
                a[s[i]] = t[i]
                b[t[i]] = s[i]
            else:
                return False
            i+=1

        return True
print(Solution().isIsomorphic('aac','bbb'))
