/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function(s) {
	let hash = {};
  for(let i in s){
  	if(hash[s[i]]) hash[s[i]]++;
  	else hash[s[i]] = 1;
  }
  let result = 0;
  let flag = false;
  for(let i in hash){
  	if(hash[i]%2 === 0) result+=hash[i]
  	else {result+=(hash[i]-1);flag = true}
  }
  if(flag) result+=1;
  return result;
};