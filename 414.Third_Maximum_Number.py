class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        first,second,third = nums[0],None,None
        for i in range(1,len(nums)):
            if nums[i] > first:
                first,second,third = nums[i],first,second
            elif nums[i]<first:
                    if second is None:
                        second = nums[i]
                    else:
                        if nums[i]>second:
                            second,third = nums[i],second
                        elif nums[i]<second:
                            if third is None:
                                third = nums[i]
                            elif nums[i] > third:
                                third = nums[i]
        return first if third is None else third