/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
	if(s.length<=numRows||numRows===1){
		return s;
	}
	var result = [];
	var gap = (numRows-1)*2;
	for (var i = 0; i < numRows; i++) {
		var index = i;
		if (i === 0 || i === numRows-1){
			while(index<s.length){
				result.push(s[index]);
				index+=gap;
			}
		}
		else{
			while(index<s.length){
				result.push(s[index]);
				result.push(s[index+gap-2*i]);
				index+=gap;
			}
		}
	}
	return result.join('');
};
var r = convert('ABC',1);
console.log(r);