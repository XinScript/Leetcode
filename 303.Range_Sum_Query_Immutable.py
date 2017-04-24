class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.checkList = []
        if nums:
            self.checkList.append(nums[0])
            for i in range(1, len(nums)):
                self.checkList.append(self.checkList[i - 1] + nums[i])


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.checkList[j]
        else:
            return self.checkList[j]-self.checkList[i-1]



a = [-2, 0, 3, -5, 2, -1]
print(NumArray(a).sumRange(2,5))
