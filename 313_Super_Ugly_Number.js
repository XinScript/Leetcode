/**
 * @param {number} n
 * @param {number[]} primes
 * @return {number}
 */
var nthSuperUglyNumber = function(n, primes) {
  const results = [];
  let count = 0;
  let indexs = Array.from({'length':primes.length}).fill(0);
  let val = Array.from({'length':primes.length}).fill(1);
  let next = 1;
  while(count<n){
  	results.push(next);
  	next = Number.MAX_SAFE_INTEGER;
  	for(let i =0; i<primes.length;i++){
  		if(val[i] == results[count]) val[i] = results[indexs[i]++] * primes[i];  		
  		next = Math.min(val[i],next);
  	}
  	count++;
  }
  return results[results.length-1];
};

