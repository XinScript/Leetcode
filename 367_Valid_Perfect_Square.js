/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function(num) {
	if (num === 0 || num === 1) return true;
	let temp = parseInt(num / 2);
	while (temp * temp > num) {
		temp = parseInt(temp / 2);
	}
	if (temp * temp === num) return true;
	for (let i = temp + 1; i < temp * 2; i++) {
		if (i * i === num) return true;
	}
	return false;
};

