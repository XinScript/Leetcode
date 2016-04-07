class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        else:
            maxSum = tempSum = nums[0]

            for i in range(1,len(nums)):
                tempSum+=nums[i]
                if nums[i]>tempSum:
                    tempSum = nums[i]
                if tempSum>maxSum:
                    maxSum = tempSum
            return maxSum