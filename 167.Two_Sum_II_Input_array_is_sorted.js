/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
	var bs = (nums, p1, p2, n) => {
		var middle = Math.floor((p1 + p2)/2);
		if (nums[middle] < n) {	
			if (middle + 1 <= p2) return bs(nums, middle + 1, p2, n);
			return -1;
		} else if (nums[middle] > n) {
			if (middle - 1 >= p1) return bs(nums, p1, middle - 1, n);
		  return -1;
		} else return middle;
	};
	for (var i = 0 ;i<numbers.length;i++) {
		var j = i + 1;
		var toFind = target - numbers[i];
		var k = bs(numbers, j, numbers.length - 1, toFind);
		if (k !== -1) return [i+1, k+1];
	}
};