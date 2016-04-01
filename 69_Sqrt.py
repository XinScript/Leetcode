class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        left = 1
        right = x / 2
        mid = int((left + right) / 2)
        while left <= right:
            mid = int((left + right) / 2)
            if x > mid * mid:
                left = mid + 1

            elif x < mid*mid:
                right = mid-1

            else:
                return mid


        if mid*mid>x:
            return mid-1
        else:
            return mid



print(Solution().mySqrt(3))

