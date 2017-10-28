class Solution(object):

    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0
        result = c = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                c += 1
            else:
                result = max(result, c)
                c = 1
        result = max(result, c)     
        return result
