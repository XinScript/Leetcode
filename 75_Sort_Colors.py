class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right-=1
                continue

            elif nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left+=1
                i+=1
            else:
                i+=1

a = [2,0,1]
Solution().sortColors(a)
print(a)