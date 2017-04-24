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
var diameterOfBinaryTree = function(root) {
	if(!root) return 0;
	let result = 0;
	function search(node){
		if(!node) return -1;
		let left = search(node.left)+1;
		let right = search(node.right)+1;
		if(left+right>result) result=left+right;
		return Math.max(left,right);
	}
	search(root);
	return result;
};