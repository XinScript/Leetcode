# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
        	return result
        flag = False
        stack = [root]
        while stack:
        	l = len(stack)
        	temp = []
        	next_stack = []
        	for i in range(l):
      			node = stack.pop()
        		temp.append(node.val)
        		if not flag:
	        		if node.left:
	        			next_stack.append(node.left)
	        		if node.right:
	        			next_stack.append(node.right)
	        	else:
	        		if node.right:
	        			next_stack.append(node.right)
	        		if node.left:
	        			next_stack.append(node.left)
        	stack = next_stack
      		result.append(temp)
      		flag = not flag
        return result

