/**
 * @param {number} n
 * @return {number}
 */
var countNumbersWithUniqueDigits = function(n) {
	if (n === 0) return 1;
	var A = function(x, y) {
		var result = 1;
		for (var i = 1; i <= y; i++) {
			result *= x;
			x--;
		}
		return result;
	};
	var result = 1;
	for(var i = 1;i<=n;i++){
		result = result + 9*A(9,i);
	}
	return result;
};

