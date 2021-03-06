# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        def r(node):
        	if node:
        		left = r(node.left)
        		right = r(node.right)
        		self.result += abs(left-right)
        		return left+right+node.val
        	else:
        		return 0
        r(root)
        return result