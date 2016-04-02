import functools
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = functools.reduce(lambda x,y:x+y,nums)
        n = len(nums)
        return int(n*(n+1)/2-s)

