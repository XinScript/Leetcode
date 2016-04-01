class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = 0
        size = len(nums)
        for i in range(0, size):
            s = s ^ nums[i]

        #get a different digit and set other digits to 0
        diff = s & (~(s - 1))

        r1 = 0
        r2 = 0

        for i in range(0, size):
            if nums[i] & diff:
                r1 ^= nums[i]
            else:
                r2 ^= nums[i]

        return [r1, r2]

