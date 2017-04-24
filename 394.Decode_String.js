/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
	let result = "";
	let times,prefix,last=0;
	for(let i in s){
		let c = s.charCodeAt(i);
	if(c>=48&&c<=57){
		prefix=s.substring(last, i);
		last = i;
	}
	else if(c>=97&&c<=122){
		last = i;
	}
	else if(c == '['){
		times = s.substring(last, i);
		last = i+1;
	}
	else if(c == ']'){
		result += (prefix+decodeString(s.substring(last, i)).repeat(times));
		last = i+1;
	}
	console.log(result);
	return result;
	}
};

decodeString("e3[a]")
// 97 - 122
// 48 - 57
