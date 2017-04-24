/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var findFrequentTreeSum = function(root) {
  let results = [];
  let freq = {};
  function cal(node){
  	if(!node) return 0;
  	let val = node.val+cal(node.left)+cal(node.right);
  	if(freq[val]) freq[val]++;
  	else freq[val] = 1;
  	return val;
  }
  cal(root);
  let arr=[];
  for(let key in freq){
  	arr.push([key,freq[key]]);
  }
  arr.sort(function(a,b){return b[1]-a[1];});
  for(let i in arr){
  	if(arr[i][1]===arr[0][1]) results.push(parseInt(arr[i][0]));
  }
  return results;
};