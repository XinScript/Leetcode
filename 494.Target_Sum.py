class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        else:
            result = 0
            dp = [0]
            gap = 1
            for num in nums:
                for j in dp[gap-1:]:
                    dp.extend([num+j,-num+j])
                gap*=2
            for j in dp[gap-1:]:
                if j == S:
                    result+=1
            return result


a = Solution().findTargetSumWays([27,22,39,22,40,32,44,45,46,8,8,21,27,8,11,29,16,15,41,0]
,10)
print(a)
