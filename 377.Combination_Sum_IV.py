class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        arr = [1]
        for i in range(1,target+1):
            s = 0
            for num in nums:
                if i - num >= 0:
                    s+=arr[i-num]
            arr.append(s)
        return arr[target]
