class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        d = dict()
        d['R'] = d['L'] = d['U'] = d['D'] = 0
        for move in moves:
        	d[move]+=1
        if d['R'] == d['L'] and d['U'] == d['D']:
        	return True
        return False

result = Solution().judgeCircle('ULDR')
print(result)