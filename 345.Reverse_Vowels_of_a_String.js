/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
	var vowels = new Set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']);
	var arr = s.split('');
	var p1 = 0,
		p2 = s.length - 1;
	while (p1 < p2) {
		while (p1 < p2 && !vowels.has(arr[p1])){
			p1++;
		}
		while (p1 < p2 && !vowels.has(arr[p2])){
			p2--;
		}
		[arr[p1],arr[p2]] = [arr[p2],arr[p1]];
		p1++;
		p2--;
	}
	return arr.join('');
};
