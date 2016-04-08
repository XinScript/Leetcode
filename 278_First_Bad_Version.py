# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version >= 6 :
        return True
    else:
        return False


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            if isBadVersion(n):
                return 1
            else:
                return 0
        else:
            left = 1
            right = n
            while left < right:
                mid = (left + right) // 2
                if isBadVersion(mid):
                    right = mid - 1
                else:
                    left = mid + 1

            if isBadVersion(left):
                return left
            if isBadVersion(left+1):
                return left+1


print(Solution().firstBadVersion(5))
