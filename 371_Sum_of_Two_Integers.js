/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var getSum = function(a, b) {
	var s1 = a.toString(2);
	var s2 = b.toString(2);
	var s2 = [];
	var len = s1.length < s2.length ? s1.length : s2.length;
	var next = false;
	for (var i = 0; i < len; i++) {
		if (s1[i] === '1' && s2[i] === '1') {
			s3.push(next?1:0);
			next = true;
		} else if (s1[i] === '0' && s2[i] === '0') {
			s3.push(next?1:0);
			next = false;
		} else {
			s3.push(next?0:1);
			next = true;
		}
	}

};
getSum(1, 2);