class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        arrs = [nums[:]]
        for i in range(len(nums)-1):
            temp = []
            for arr in arrs:
                for k in range(i, len(nums)):
                    copy = arr[:]
                    copy[i], copy[k] = copy[k], copy[i]
                    temp.append(copy)
            arrs = temp
        return arrs

