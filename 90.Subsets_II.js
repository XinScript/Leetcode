/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
	if(nums.length===0)return [[]];
  nums.sort();
  let results = [[],[nums[0]]];
  let s = new WeakSet();
  s.add([nums[0]])
  let p = nums[1] === nums[0]?1:0;

  for(let i =1;i<nums.length;i++){
  	if(nums[i]===nums[i-1]){
  		const l = results.length;
  		for(let k=p;k<l;k++){
  			results.push(results[k].concat(nums[i]));
  		}
  		p = l;
  	}
  	else{
  		p = results.length;
	  	for(let j in results){
	  		let temp = results[j].concat(nums[i]);
	  		results.push(temp);
	  	}
	  }
  }
  return results;
};
