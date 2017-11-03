class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        def backtrack(string,left,right):
        	if len(string) == n*2:
        		answer.append(string)
        		return
        	if left < n:
        		backtrack(string+"(",left+1,right)
        	if right < left:
        		backtrack(string+")",left,right+1)
       	backtrack("",0,0)
       	return answer

print(Solution().generateParenthesis(3))       	