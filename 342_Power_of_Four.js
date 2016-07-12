/**
 * @param {number} num
 * @return {boolean}
 */
var isPowerOfFour = function(num) {
	if (num === 0) return false;
	return Math.sqrt(num) === (num>>(num.toString(2).length-1)/2);
};
