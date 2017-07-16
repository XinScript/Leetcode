# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
        	return ''
        else:
        	left = self.tree2str(t.left)
        	right = self.tree2str(t.right)
        	left = '({0})'.format(left) if left else ''
        	right = '({0})'.format(right) if right else ''
        	if not left and right:
        		return str(t.val)+'()'+right
        	return str(t.val)+left+right
