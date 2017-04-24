/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
	var hash = {};
	for(var i = 0;i<nums.length;i++){
		if(hash[target-nums[i]]){
			return [hash[target-nums[i]]-1,i];
		}
		hash[nums[i]] = i+1;
	}
};

