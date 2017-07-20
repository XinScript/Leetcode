# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count = 0
        def r(node):
        	if not node:
        		return []
        	left = r(node.left)
        	right = r(node.right)
        	for i in range(len(left)):
        		if left[i] == sum:
        			self.count+=1
        		left[i]+=node.val
        	for i in range(len(right)):
        		if right[i] == sum:
        			self.count+=1
        		right[i]+=node.val
        	return left+right+[node.val]
        whole = r(root)
        for i in range(len(whole)):
        		if whole[i] == sum:
        			self.count+=1
     
        return self.count

