/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
	var max = 0;
	var count = 0;
  for(var i in nums){
  	if(nums[i] === 1) count++;
  	else{
  		max = max < count?count:max;
  		count = 0;
  	}
  }  
  max = max < count?count:max;
  return max;
};
