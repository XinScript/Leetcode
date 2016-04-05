class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        else:
            result = [1,1]
            for i in range(2,n+1):
                s = 0
                for j in range(0,i):
                    s += result[i-j-1]*result[j]
                result.append(s)
            return result.pop()

print(Solution().numTrees(3))

