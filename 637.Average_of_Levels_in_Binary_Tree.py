# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        stack = []
        answers = []
        temp = 0
        count = 0
        current_level = 1
        stack.append((root,1))
        while stack:
        	node,level = stack.pop(0)
        	print('{0},{1}'.format(node.val,level))
        	if current_level == level:
        		temp+=node.val
        		count+=1
        	else:
        		answers.append(float(temp)/count)
        		print(float(temp)/count)
        		count = 1
        		temp = node.val
        		current_level += 1
        	if node.left:
        		stack.append((node.left,level+1))
        	if node.right:
        		stack.append((node.right,level+1))
        answers.append(float(temp)/count)
        return answers
