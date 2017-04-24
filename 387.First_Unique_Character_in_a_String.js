/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
	let hash = {};
	let count = 0;
	for(let w of s){
  	if(!hash[w]) {hash[w] = [count,1];count++}
  	else hash[w][1]++;
	}
  let arr = [];
  console.log(hash)
  for(let i in hash){
  	if(hash[i][1]==1) arr.push(hash[i]);
  }
  if(!arr.length) return -1;
  for()
};
firstUniqChar("dddccdbba");