class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        result = {0:0}
        for i in coins:
            result[i] = 1
        for i in range(1,amount+1):
            s = []
            for coin in coins:
                a = result.get(i-coin,-1)
                if a!=-1:
                    s.append(a)
            temp = min(s) if len(s)!=0 else 0
            if temp !=0:
                if result.get(i):
                    result[i] = min(result[i],temp+1)
                else:
                    result[i] = temp+1
        return result.get(amount,-1)
