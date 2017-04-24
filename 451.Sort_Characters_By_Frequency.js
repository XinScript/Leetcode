/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function(s) {
	let hash = {};
	let arr = [];
	for(let i in s){
		if(hash[s[i]]) hash[s[i]]++;
		else hash[s[i]] = 1;
	}
	for(let key in hash){
		arr.push([hash[key],key]);
	}
	arr.sort((a,b)=>b[0]-a[0]);
	let results = [];
	for(let i in arr){
		results.push(arr[i][1].repeat(arr[i][0]))
	}
	return results.join('');
};

frequencySort('');
