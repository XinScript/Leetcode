/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var getMinimumDifference = function(root) {
  let result = [];
  function search(node){
  	if(!node) return;
  	search(node.left);
  	result.push(node.val);
  	search(node.right);
  }
  search(root);
  let min = result[1]-result[0];
  for(let i =2;i<result.length;i++){
  	if(result[i]-result[i-1]<min) min = result[i]-result[i-1];
  	if(min === 0) return 0;
  }
  return min;
};