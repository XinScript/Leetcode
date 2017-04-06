/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
	if (nums.length<=1) return -1;
	for(let i in nums){
		if(nums[Math.abs(nums[i])-1]>0) nums[Math.abs(nums[i])-1]=-nums[Math.abs(nums[i])-1];
		else return Math.abs(nums[i]);
	}
	let slow = 0;
	let fast = nums[nums[0]];
	while(slow!==fast){
		slow = nums[slow];
		fast = nums[nums[fast]];
	}
	fast = 0;
	while(fast!=slow){
		fast = nums[fast];
		slow = nums[slow];
	}
	return slow
};