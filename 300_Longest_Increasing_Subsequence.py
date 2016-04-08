class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        elif l == 1:
            return 1
        else:
            result = [1 for i in range(0, len(nums))]
            result[0] = 1
            for i in range(1, l):
                ans = result[i]
                for j in range(0, i):
                    if nums[j] < nums[i]:
                        if result[j] + 1 > ans:
                            ans = result[j] + 1
                result[i] = ans

            maxCount = 1
            for i in result:
                if i > maxCount:
                    maxCount = i
            return maxCount