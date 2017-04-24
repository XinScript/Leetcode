class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        output = [1]
        left = 1
        for i in range(1,size):
            left*=nums[i-1]
            output.append(left)

        right = 1
        for i in range(size-2,-1,-1):
            right*=nums[i+1]
            output[i]*=right
        return output


print(Solution().productExceptSelf([1,2,0,4]))