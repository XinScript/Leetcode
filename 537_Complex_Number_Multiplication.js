/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var complexNumberMultiply = function(a, b) {   
	let arrA = a.split(/[+i]/);
	let arrB = b.split(/[+i]/);
	let c = arrA[0]*arrB[0]-arrA[1]*arrB[1];
	let d = arrA[0]*arrB[1]+arrA[1]*arrB[0];
	return c.toString()+'+'+d.toString()+'i';
};

console.log(complexNumberMultiply('1+-1i','1+-1i'))

