class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums:
                result = [[nums[0]]]
                for i in range(1,len(nums)):
                    new = []
                    for j in result:
                        for k in range(0,len(j)+1):
                            temp = list(j)
                            temp.insert(k,nums[i])
                            new.append(temp)
                    result = new
                return result
        else:
            return [[]]



print(Solution().permute([1,2,3,4]))

