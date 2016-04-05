class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.quene = []

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        s = 0
        for x in range(i,j+1):
            s+=self.nums[i]
        return s
# Your NumArray object will be instantiated and called as such:
numArray = NumArray([1,2,3,4,5])
print(numArray.sumRange(0, 1))
print(numArray.sumRange(1, 2))