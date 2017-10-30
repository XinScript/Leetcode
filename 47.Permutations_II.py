class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        arrs = [nums[:]]
        s = set()
        for i in range(len(nums)-1):
            temp = []
            for arr in arrs:
                for k in range(i, len(nums)):
                    copy = arr[:]
                    if i == k or arr[k] not in s:
                        s.add(arr[k])
                        copy[i], copy[k] = copy[k], copy[i]
                        temp.append(copy)
                s.clear()
            arrs = temp
        return arrs

