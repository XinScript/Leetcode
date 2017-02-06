/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
	nums.sort((a, b) => a - b);
	var closest = false;
	for (var i = 0; i < nums.length - 2; i++) {
		if (i === 0 || (i > 0 && nums[i] != nums[i - 1])) {
			var low = i + 1;
			var high = nums.length - 1;
			while (low < high) {
				sum = nums[i] + nums[low] + nums[high];
				if(closest === false) closest = sum;
				if (Math.abs(sum-target) < Math.abs(closest-target)) closest = sum;
					if (sum === target) {
						return sum;
					} else if (sum -target > 0) high--;
				else low++;
			}
		}
	}
	return closest;
};

console.log(threeSumClosest([0,0,0],1));