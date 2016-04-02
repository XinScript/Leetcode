# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return False
        else:

            left = self.lowestCommonAncestor(root.left,p,q)
            right = self.lowestCommonAncestor(root.right,p,q)
            if isinstance(left,TreeNode):
                return left
            elif isinstance(right,TreeNode):
                return right
            elif left and right:
                return root
            elif left or right:
                if root is p:
                    return p
                elif root is q:
                    return q
                else:
                    return True
            else:
                if root is p or root is q:
                    return True
                else:
                    return False





