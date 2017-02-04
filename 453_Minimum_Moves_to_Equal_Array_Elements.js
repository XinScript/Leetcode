/**
 * @param {number[]} nums
 * @return {number}
 */
var minMoves = function(nums) {
	var sum = 0;
	var m = Math.min(...nums);
	for(var i in nums){
		sum+=nums[i];
	}
	return sum-nums.length*m;
};
