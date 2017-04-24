/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
	var results = [];
	for (var i = 1,buzz=0,fizz=0; i <= n; i++) {
		buzz++;
		fizz++;
		if(buzz === 5 && fizz === 3){
			results.push('FizzBuzz');
			buzz=0;
			fizz = 0;
		}
		else if(fizz === 3){
			results.push('Fizz');
			fizz = 0;
		}
		else if(buzz === 5){
			results.push('Buzz');
			buzz = 0;
		}
		else results.push(i.toString());
	}
	return results;
};
