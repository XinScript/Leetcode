class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        result = [0]
        for i in range(1,amount+1):
            s = []
            if i in coins:
                result.append(1)
            else:
                result.append(-1)
            for coin in coins:
                if i - coin > 0:
                    a = result[i-coin]
                    if a!=-1:
                        s.append(a)
            temp = min(s) if len(s)>0 else -1
            if temp !=-1:
                if result[i]!=-1:
                    result[i] = min(result[i],temp+1)
                else:
                    result[i] = temp+1
        return result[amount]
print(Solution().coinChange([186,419,83,408]
,6249))
