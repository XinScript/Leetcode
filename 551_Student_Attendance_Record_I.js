/**
 * @param {string} s
 * @return {boolean}
 */
var checkRecord = function(s) {
	let count1 = 0;
	let count2 = 0;
	for (let i in s) {
		console.log(i)
		if (s[i] === 'L') {
			count2++;
			if (count2>2) return false;
		} else {
			if (s[i] === 'A') {
				count1 += 1;
				if (count1 > 1) return false;
			}
			count2=0;
		}
	}
	return true;
};
