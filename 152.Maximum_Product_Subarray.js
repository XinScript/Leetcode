/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
	let max = nums[0];
	for(let i = 1,imax = max,imin = max;i<nums.length;i++){
		if(nums[i]<0){
			[imax,imin]=[imin,imax];
		}
		imax = Math.max(nums[i],imax*nums[i]);
		imin = Math.min(nums[i],imin*nums[i]);
		max = Math.max(imax,max);
	}
	return max;
};
console.log(maxProduct([2,3,-2,4,-2,2]));