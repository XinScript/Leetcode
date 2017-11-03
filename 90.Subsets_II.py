class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        nums.sort()
        def backtrack(arr, index):
            if index < len(nums):
                answer.append(arr)
                if index < len(nums):
                    for i, ele in enumerate(nums[index+1:]):
                        if i != 0 and ele == nums[index+i]:
                            continue
                        else:
                            backtrack(arr[:]+[ele], index+i+1)
                else:
                    return
        backtrack([], -1)
        return answer

print(Solution().subsetsWithDup([1, 2, 2,2]))
