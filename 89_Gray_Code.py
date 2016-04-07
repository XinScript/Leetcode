class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]

        if n == 1:
            return [0,1]
        else:
            result = [0,1]
            for i in range(1,n):
                num = count = 2**i
                for j in range(0,num):
                    result.append(result[count-1]+num)
                    count-=1

            return result

print(Solution().grayCode(3))



