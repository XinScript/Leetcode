var checkPerfectNumber = function(num) {
  let ceil = Math.ceil(Math.sqrt(num));
  let result = [1];
  if(ceil*ceil === num) result.push(ceil);
  for(let i = 2;i<ceil;i++){
  	if(num%i === 0){
  		result.push(i);
  		result.push(num/i);
  	}
  }
  return result.reduce((a,b)=>a+b,0) === num
};
console.log(checkPerfectNumber(28))