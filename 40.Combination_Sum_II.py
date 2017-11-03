class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        answer = []
        candidates.sort();
        print(candidates)
        def backtrack(arr,index):
        	if sum(arr) > target:
        		return
        	elif sum(arr) < target:
        		for i,ele in enumerate(candidates[index+1:]):
        			if i!=0 and ele==candidates[index+i]:
        				continue
        			else:
        				backtrack(arr[:]+[ele],index+i+1)
        	else:
        		answer.append(arr)
        		return
       	backtrack([],-1)
       	return answer
print(Solution().combinationSum2([2,5,2,1,2],5));