/**
 * @param {string} s
 * @return {number}
 */
var calculate = function(s) {
	const ops = {
		'+': (a, b) => a + b,
		'-': (a, b) => a - b,
		'*': (a, b) => a * b,
		'/': (a, b) => a / b,
		isOpts: (s) => ['+', '-', '*', '/'].includes(s)
	};
	const prior = {
		'+': 1,
		'-': 1,
		'*': 2,
		'/': 2
	};

	function cal() {
		let op = s1.pop()
		let b = parseInt(s2.pop());
		let a = parseInt(s2.pop());
		s2.push(ops[op](a, b));

	};

	let s1 = [];
	let s2 = [];
	let temp = '';
	for (let i in s) {
		if (ops.isOpts(s[i])) {
			s2.push(temp);
			temp = '';
			if (s1.length === 0 || prior[s1[s1.length - 1]] < prior[s[i]]) s1.push(s[i]);
			else {
				while(prior[s1[s1.length - 1]] >= prior[s[i]]){cal()}
				s1.push(s[i]);
			}
		} else {
			temp+=s[i];
		}
	}
	s2.push(temp);
	while (s1.length) {
		cal();
	}
	return parseInt(s2.pop());
};
