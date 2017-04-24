/**
 * @param {string} s
 * @return {number}
 */
var countSegments = function(s) {
	// s=s.trim();
	// return s === '' ? 0 : s.split(/\s+/).length;
	let flag = true;
	let count = 0;
	for(let i in s){
		if(s.charCodeAt(i) !== 32&&flag) {
			count ++;
			flag = false;
		}
		if(s.charCodeAt(i) === 32) flag = true;
	}
	return count;
};
