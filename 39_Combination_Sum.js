/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
	if (candidates.length === 0) return [];
	var result = [];
	for (var i = candidates.length - 1; i >= 0; i--) {
		var sum = candidates[i];
		var current = [sum];
		if (sum > target) continue;
		else if (sum === target) {
			result.push(current);
			continue;
		}
		while (sum !== target) {
			var sub = combinationSum(candidates.slice(0, i + 1), target - sum);
			if (sub.length === 0) break;
			sub.forEach(function(arr) {
				result.push(arr.concat(current));
			});
			break;
		}
	}
	return result;
}
