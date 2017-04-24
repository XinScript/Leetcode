class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        isPrime = [True for i in range(0, n)]
        i = 2
        while i * i < n:
            if not isPrime[i]:
                i+=1
                continue
            j = i * i
            while j < n:
                isPrime[j] = False
                j += i
            i += 1

        count = 0
        for i in isPrime:
            if i:
                count += 1
        return count - 2


print(Solution().countPrimes(499979))
