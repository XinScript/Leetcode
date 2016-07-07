/**
 * @param {string} s
 * @return {string}
 */
var reverseString = function(s) {
	var len = s.length-1;
	var stack = [];
	for (var i = len; i >= 0; i--) {
		stack.push(s[i]);
	}
	return stack.join('');
};


