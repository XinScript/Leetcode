/**
 * @param {string} s
 * @return {number}
 */
// "(1+(4+5+2)-3)+(6+8)" = 23
var calculate = function(s) {
	function cal(op) {
		let b = numstack.pop();
		let a = numstack.pop();
		let c;
		if (op === '+') {
			c = a + b;
		}
		if (op === '-') {
			c = a - b;
		}
		numstack.push(c);
	}
	let numstack = [];
	let opstack = [];
	let temp = '';
	for (let i in s) {
		if (s[i] === ' ') {
			continue;
		}
		if (isNaN(parseInt(s[i]))) {
			console.log(numstack);
			console.log(opstack);
			if(temp!==''){
				numstack.push(parseInt(temp));
				temp = '';
			}
			if (['+', '-'].includes(s[i])) {
				if (opstack.length === 0 || opstack[opstack.length - 1] === '(') opstack.push(s[i]);
				else {
					cal(opstack.pop());
					opstack.push(s[i]);
				}
			} else if (s[i] === '(') {
				opstack.push(s[i]);
			} else if (s[i] === ')') {
				let op = opstack.pop();
				while (op !== '(') {
					cal(op);
					op = opstack.pop();
				}
			}
		} else {
			temp += s[i];
		}

	}
	if(temp!=='')numstack.push(parseInt(temp));
	while (opstack.length > 0) cal(opstack.pop());
	return numstack.pop();
};
