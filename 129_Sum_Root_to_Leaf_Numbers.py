# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [0]
        def cal(root,val):
            if root:
                if root.left and root.right:
                    cal(root.left,10*val+root.val)
                    cal(root.right,10*val+root.val)
                elif root.left:
                    cal(root.left,10*val+root.val)
                elif root.right:
                    cal(root.right,10*val+root.val)
                else:
                    result[0]+=10*val+root.val

        cal(root,0)
        return result[0]


