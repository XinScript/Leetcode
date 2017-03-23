/**
 * @param {number} n
 * @return {number}
 */
var nthUglyNumber = function(n) {
	let dp = [1];
	let i2 = i3 = i5 = 0;
	while (n > 1) {
		[u2,u3,u5] = [dp[i2]*2,dp[i3]*3,dp[i5]*5];
		let min = Math.min(u2,u3,u5);
		if(min === u2) i2++;
		else if(min === u3) i3++;
		else i5++;
		dp.push(min);
		n--;
	}
	return dp.pop();
};