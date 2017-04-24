
/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
	if(digits.length===0)return [];
	let map = {
		'1': ['*'],
		'2': ['a', 'b', 'c'],
		'3': ['d', 'e', 'f'],
		'4': ['g', 'h', 'i'],
		'5': ['j', 'k', 'l'],
		'6': ['m', 'n', 'o'],
		'7': ['p', 'q', 'r', 's'],
		'8': ['t', 'u', 'v'],
		'9': ['w', 'x', 'y', 'z']
	};
	let dp = map[digits[0]].slice();
	for (let i = 1; i < digits.length; i++) {
		let arr = [];
		for (let j in map[digits[i]]) {
			let copy = [];
			for (let k in dp) {
				copy.push(dp[k]+map[digits[i]][j]);
			}
			arr = arr.concat(copy);
		}
		dp = arr;
	}
	return dp;
};

