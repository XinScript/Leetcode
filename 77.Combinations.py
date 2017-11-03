class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        answer = []
        def backtrack(arr):
        	if len(arr) == k:
        		answer.append(arr)
        		return
        	if len(arr) == 0 or arr[-1] != n:
        		end = arr[-1]+1 if len(arr) != 0 else 1
        		for i in range(end,n+1):
        			backtrack(arr[:]+[i])
        	else:
        		return
       	backtrack([])
       	return answer
