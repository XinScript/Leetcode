# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def height(node):
            if node is None:
                return 0
            else:
                left = height(node.left)
                right = height(node.right)
                if left == -1 or right == -1:
                    return -1
                else:
                    if abs(left-right) > 1:
                        return -1
                    else:
                        return max(left,right)+1

        result = height(root)

        if result!=-1:
            return True
        else:
            return False
