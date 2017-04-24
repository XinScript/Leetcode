# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        result = []
        def traveral(root):
            if root is None:
                return
            else:
                traveral(root.left)
                result.append(root.val)
                traveral(root.right)

        traveral(root)

        for i in range(1,len(result)):
            if result[i]<=result[i-1]:
                return False

        return True
