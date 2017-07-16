class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums)*len(nums[0])!=r*c:
        	return nums
        whole = []
        for arr in nums:
        	whole+=arr
        i = 0
        result = []
        while i < len(whole):
        	result.append(whole[i:i+c])
        	i+=c
        return result




