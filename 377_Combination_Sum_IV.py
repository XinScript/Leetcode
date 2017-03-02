class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        arr = {0:1}
        for i in range(1,target+1):
            for num in nums:
                if i - num >= 0:
                    arr[i] = arr.setdefault(i,0) + arr.setdefault(i-num,0)
        return arr.setdefault(target,0)
        
print(Solution().combinationSum4([1,2,3],3))
