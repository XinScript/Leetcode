class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = []
        first_row = [grid[0][0]]
        for i in range(1,len(grid[0])):
            first_row.append(grid[0][i]+first_row[i-1])
        result.append(first_row)
        temp = []
        for i in range(1,len(grid)):
            temp = [grid[i][0]+result[i-1][0]]
            result.append(temp)
        print(result)

        for i in range(1,len(grid)):
            for j in range(1,len(grid[i])):
                result[i].append(min(result[i][j-1],result[i-1][j])+grid[i][j])

        return result.pop().pop()

print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
