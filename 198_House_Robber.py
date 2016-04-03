class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unRob = rob = 0

        for i in nums:
            if unRob+i > rob:
                temp = rob
                rob= i + unRob
                unRob = temp
            else:
                unRob = rob

        return max(unRob, rob)


print(Solution().rob([1, 2]))
