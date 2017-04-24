class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        else:
            j = 2
            s = "1"
            while j <= n:
                result = ""
                current = s[0]
                count = 0
                for i in range(0,len(s)):
                    if s[i] == current:
                        count+=1
                    else:
                        result=result+str(count)+current
                        current = s[i]
                        count=1
                result=result+str(count)+current
                s = result
                j+=1
            return s

print(Solution().countAndSay(30))

