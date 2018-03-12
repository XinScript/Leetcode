class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        answer = [0, 0]
        dp = [[False for i in range(n)] for j in range(n)]
        for j in range(0, n):
            for i in range(0, j + 1):
                if i == j:
                    dp[i][j] = True
                elif i + 1 == j:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j] and j - i > answer[1] - answer[0]:
                    answer = [i, j]
        return s[answer[0]:answer[1] + 1]
