class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        d = {}
        for i,num in enumerate(nums):
            d[num] = i
        for num in findNums:
            p = d[num] + 1
            while p < len(nums):
                if nums[p] > num:
                    result.append(nums[p])
                    break
                p+=1
            result.append(-1) if p == len(nums) else None
        return result