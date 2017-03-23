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
var largestValues = function(root) {
	let results = [];

	function find(node, layer) {
		if (!node) return;
		if (layer > results.length) {
			results.push(node.val);
		} else {
			if (node.val > results[layer - 1]) results[layer - 1] = node.val
		}
	find(node.left,layer+1);
	find(node.right,layer+1);
	}
	find(root, 1);
	return results;
};