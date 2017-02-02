/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var hammingDistance = function(x, y) {
  var c = (x^y).toString(2);
  var num = 0;
  for(var i in c){
  	if(c[i] === '1'){
  		num ++;
  	}
  }  
  return num;
};