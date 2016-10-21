/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
	if (s.length === 0) return true;
	var c = -1;
	for (var i in s) {
		var n = t.indexOf(s[i]);
		if(n === -1) return false;
		t = t.substring(n+1,t.length);
	}
	return true;
};

