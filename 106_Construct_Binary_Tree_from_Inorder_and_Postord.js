/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var buildTree = function(inorder, postorder) {
  	if(inorder.length === 0) return null;
  	const val = postorder[postorder.length-1];
  	const node = new TreeNode(val);
  	const index = inorder.indexOf(val);
  	node.left = buildTree(inorder.slice(0,index),postorder.slice(0, index));
  	node.right= buildTree(inorder.slice(index+1),postorder.slice(index,postorder.length-1));
  	return node;
};
