/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
	if (prices.length < 2) {
		return 0;
	}
	var result = 0;
	var base;
	prices.forEach((price) => {
		var gap = price - base;
		if (gap > 0) {
			result = gap > result ? gap : result;
		} else {
			base = price;
		}
	});
	return result;
};
var r = maxProfit([7, 1, 5, 3, 6, 4]);
console.log(r)
