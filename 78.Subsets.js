/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
	let results = [[]];
	let gap = 1;
	for(let i in nums){
		for (let j = 0; j < gap; j++) {
			let copy = results[j].slice();
			copy.push(nums[i]);
			results.push(copy);
		}
		gap*=2;
	}
	return results;
};

