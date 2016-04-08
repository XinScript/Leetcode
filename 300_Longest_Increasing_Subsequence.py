class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        elif l == 1:
            return 1
        else:
            result = [1 for i in range(0, len(nums))]
            result[0] = 1
            for i in range(1, l):
                ans = result[i]
                for j in range(0, i):
                    if nums[j] < nums[i]:
                        if result[j] + 1 > ans:
                            ans = result[j] + 1
                result[i] = ans

            maxCount = 1
            for i in result:
                if i > maxCount:
                    maxCount = i
            return maxCount

    def lengthOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binarySearch(left, right, nums, n):
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < n:
                    left = mid + 1
                elif nums[mid] > n:
                    right = mid - 1
                else:
                    left = mid
                    break
            if nums[left] < n:
                return left
            else:
                return left-1

        l = len(nums)
        if l == 0:
            return 0
        elif l == 1:
            return 1
        else:
            result = [1 for i in range(0, len(nums))]
            result[0] = 1
            temp = [None,nums[0]]
            for i in range(1, l):
                j = binarySearch(1,len(temp)-1,temp,nums[i])
                if j == len(temp)-1:
                    result[i] = result[i-1]+1
                    temp.append(nums[i])

                else:
                    result[i] = result[i-1]
                    if j == 0 and nums[i]<temp[1]:
                        temp[1] = nums[i]
                    if temp[j+1]>nums[i]:
                        temp[j+1] = nums[i]

            maxCount = 1
            for i in result:
                if i > maxCount:
                    maxCount = i
            return maxCount
