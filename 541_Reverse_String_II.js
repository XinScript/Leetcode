/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var reverseStr = function(s, k) {
	s = s.split('');
	gap = k * 2;

	function reverse(p1, p2) {
		while (p1 < p2) {
			[s[p1], s[p2]] = [s[p2], s[p1]];
			p1++;
			p2--;
		}
	}
	for (p1 = 0, p2 = Math.min(s.length - 1, p1 + k - 1); p1 < s.length; p1 += gap, p2 = Math.min(s.length - 1, p1 + k - 1)) {
		reverse(p1, p2);
	}
	return s.join('');
};
