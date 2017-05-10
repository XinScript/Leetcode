# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def compare(a,b):
        	if not a and not b:
        		return True
        	elif a and b:
        		if a.val == b.val:
        			return compare(a.left,b.left) and compare(a.right,b.right)
        		else:
        			return False
        	else:
        		return False

        stack = [s]

        while stack:
        	current = stack.pop()
        	if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)
            result = compare(current,t)
            if result:
                return True
        return False

