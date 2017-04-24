class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        divide = 1
        count = 0
        while True:
            divide *= 5
            r = int(n / divide)
            if r >= 1:
                count += r
            else:
                break
        return count
