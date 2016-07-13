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

// var rightSideView = function(root) {
// 	if (root === null || root.length === 0) {
// 		return [];
// 	}

// 	var stack = [];
// 	var result = [];
// 	stack.push(root);
// 	var currentCount = 1;
// 	var nextCount = 0;
// 	while (stack.length) {
// 		var node = stack.shift();
// 		if (currentCount) {
// 			currentCount--;
// 		} else {
// 			currentCount = nextCount - 1;
// 			nextCount = 0;
// 		}
// 		if (currentCount === 0) {
// 			result.push(node.val);
// 		}
// 		if (node.left) {
// 			stack.push(node.left);
// 			nextCount++;
// 		}
// 		if (node.right) {
// 			stack.push(node.right);
// 			nextCount++;
// 		}
// 	}
// 	return result;
// };

// function node(val) {
// 	this.val = val;
// 	this.left = this.right = null;
// }

// console.log(rightSideView(new node(1)));