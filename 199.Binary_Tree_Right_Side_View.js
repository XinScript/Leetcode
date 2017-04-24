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

var rightSideView = function (root) {
	if (root === null || root.length === 0) {
		return [];
	}
	var seq = [];

	function rc(node, level) {
		if (node === null) {
			return;
		}
		if (!seq[level]) {
			seq[level] = node.val;
		}
		rc(node.right,level+1);
		rc(node.left,level+1);
	}
	rc(root, 0);

	return seq;
};
