class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = set()
        while n!=1:
            if n not in d:
                d.add(n)
                s = 0
                for i in str(n):
                    j = int(i)
                    s+=j*j
                n = s
            else:
                return False
        return True

print(Solution().isHappy(7))

