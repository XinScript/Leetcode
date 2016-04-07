class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        maxtrix = []
        for i in range(0,m):
            row = []
            for j in range(0,n):
                if j == 0 or i == 0:
                    row.append(1)
                else:
                    row.append(maxtrix[i-1][j]+row[j-1])
            maxtrix.append(row)
        return maxtrix[m-1][n-1]







