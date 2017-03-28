/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
    if(inorder.length === 0) return null;
  	const val = preorder[0];
  	const node = new TreeNode(val);
  	const index = inorder.indexOf(val);
  	node.left = buildTree(preorder.slice(1,index+1),inorder.slice(0, index));
  	node.right= buildTree(preorder.slice(index+1),inorder.slice(index+1));
  	return node;
};