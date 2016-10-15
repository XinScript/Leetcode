/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {
	var result = 0;
	for (var i in s) {
		result = result ^ s[i].charCodeAt(0) ^ t[i].charCodeAt(0);
	}
	return String.fromCharCode(result ^ t[t.length-1].charCodeAt(0));
};
var r = findTheDifference('ab','abc');
console.log(String.fromCharCode(r));