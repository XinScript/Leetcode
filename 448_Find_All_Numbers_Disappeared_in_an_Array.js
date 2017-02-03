/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
	var results = [];
for(var i in nums){
	var index = Math.abs(nums[i])-1;
	if(nums[index]>0) nums[index] = -nums[index];
}
for(var i in nums){
	if(nums[i]>0) results.push(parseInt(i)+1);
}
return results;
};
console.log(findDisappearedNumbers([1,2,3,4,4]));
