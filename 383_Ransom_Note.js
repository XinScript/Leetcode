/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function(ransomNote, magazine) {
	var s = Array.from({length:26}).fill(0);
	for(var i in magazine){
		s[magazine[i].charCodeAt(0)-97]++;
	}
	for(var j in ransomNote){
		s[ransomNote[j].charCodeAt(0)-97]--;
		if(s[ransomNote[j].charCodeAt(0)-97]<0) return false;
	}
	return true;
};
