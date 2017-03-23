class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        arr = sorted(nums,reverse=True);
        index = [nums.index(x) for x in arr]
        for i in range(len(arr)):
            if i == 0:
                nums[index[i]] = 'Gold Medal'
            elif i == 1:
                nums[index[i]] = 'Silver Medal'
            elif i == 2:
                nums[index[i]] = 'Bronze Medal'
            else:
                nums[index[i]] = str(i+1)
        return nums
