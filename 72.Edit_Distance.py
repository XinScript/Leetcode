class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        length1 = len(word1)+1
        length2 = len(word2)+1
        dp = [[j for j in range(length2)]]
        for i in range(1,length1):
        	current = [i]
        	for j in range(1,length2):
        		if word1[i-1] == word2[j-1]:
        			current.append(dp[i-1][j-1])
        		else:
        			current.append(min(dp[i-1][j],current[j-1],dp[i-1][j-1])+1)
        # return dp[length1-2][length2-2]
        # for i in range(1,length1):
        # 	dp.append([i]+[0 for j in range(1,length2)])
        # for i in range(1,length1):
        # 	for j in range(1,length2):
        # 		if word1[i-1] == word2[j-1]:
        # 			dp[i][j] = dp[i-1][j-1]
        # 		else:
        # 			dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        # return dp[length1-1][length2-1]

print(Solution().minDistance('aaa','bbb'))