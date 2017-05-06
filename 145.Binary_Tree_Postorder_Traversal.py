# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        tags = {}
        def load(node):
        	while node:
        		stack.append(node)
        		tags[node] = 1
        		node = node.left
        load(root)
        while stack:
        	current = stack.pop()
        	tags[current]+=1
        	if tags[current] == 3:
        		result.append(current.val)
        	elif tags[current] == 2:
	        	if current.right:
	        		stack.append(current)
	        		load(current.right)
	        	else:
	        		result.append(current.val)
        return result

