# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        arr = []
        s = 0
        def load(node):
        	if not node:
        		return
        	load(node.left)
        	arr.append(node)
        	load(node.right)
        load(root)
        while arr:
        	node = arr.pop()
        	temp = s + node.val
        	node.val += s
        	s = temp
        return root