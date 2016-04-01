class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = nums[0]
        size = len(nums)
        for i in range(1,size):
            s = s^nums[i]
        return s