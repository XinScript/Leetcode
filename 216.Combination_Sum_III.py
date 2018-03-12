class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        s = [1,2,3,4,5,6,7,8,9]
        rs = []
        def backtrack(arr,index):
        	if len(arr) == k:
        		if sum(arr) == n:
        			rs.append(arr)
        		return
        	for i,ele in enumerate(s[index+1:]):
        		backtrack(arr+[ele],index+i+1)
        	return
       	backtrack([],-1)
       	return rs

print(Solution().combinationSum3(3,9))

