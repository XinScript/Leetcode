
# var subsets = function(nums) {
# 	let results = [[]];
# 	let gap = 1;
# 	for(let i in nums){
# 		for (let j = 0; j < gap; j++) {
# 			let copy = results[j].slice();
# 			copy.push(nums[i]);
# 			results.push(copy);
# 		}
# 		gap*=2;
# 	}
# 	return results;
# };


 class Solution:
     def subsets(self, nums):
         """
         :type nums: List[int]
         :rtype: List[List[int]]
         """
         answer = []
         def backtrack(arr,index):
             if index < len(nums):
                 answer.append(arr)
                 if index < len(nums):
                 	for i,ele in enumerate(nums[index+1:]):
                 		backtrack(arr[:]+[ele],index+i+1)
                 else:
                 	return
         backtrack([],-1)
         return answer
