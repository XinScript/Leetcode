/**
 * @param {number} n
 * @return {number}
 */
var integerBreak = function(n) {
	if (n === 2) return 1;
	if (n === 3) return 2;
	if (n === 4) return 4;
	var remain = n % 3;
	var times = Math.floor(n / 3);
	
	if (remain === 0) return Math.pow(3,times);
	if (remain === 1) return Math.pow(3,times-1)*4;
	return Math.pow(3,times)*2;
};
