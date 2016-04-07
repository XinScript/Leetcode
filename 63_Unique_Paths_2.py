class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    if i == 0 and j == 0:
                        obstacleGrid[i][j] = 1
                    elif i == 0:
                        obstacleGrid[i][j] = obstacleGrid[i][j-1]
                    elif j == 0:
                        obstacleGrid[i][j] = obstacleGrid[i-1][j]
                    else:
                        obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]

        return obstacleGrid[m - 1][n - 1]

print(Solution().uniquePathsWithObstacles([[0]]))
