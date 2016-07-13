/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
	var mapper = {};
	var seq = [];
	var result = [];
	for (var i in nums) {
		if (mapper[nums[i]]) {
			mapper[nums[i]]++;
		} else {
			mapper[nums[i]] = 1;
		}
	}
	for (var key in mapper) {
		seq.push({
			key: key,
			value: mapper[key]
		});
	}
	seq.sort((a, b) => {
		return b.value - a.value;
	});

	for (var i = 0; i < k; i++) {
		result.push(parseInt(seq[i]['key']));
	}
	return result;
};

