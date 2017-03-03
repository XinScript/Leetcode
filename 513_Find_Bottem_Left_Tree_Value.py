# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_layer = 1
        self.result = root.val
        def traverse(node,layer):
            if not node:
                return 0
            if layer>self.max_layer:
                self.max_layer = layer
                self.result = node.val
            traverse(node.left,layer+1)
            traverse(node.right,layer+1)
        traverse(root,1)
        return self.result
