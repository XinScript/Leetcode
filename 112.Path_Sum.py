# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def add(root,val,sum):
            if root is None:
                return False
            else:
                if root.left is None and root.right is None:
                    if val+root.val == sum:
                        return True
                    else:
                        return False

                left = add(root.left,root.val+val,sum)
                right = add(root.right,root.val+val,sum)
                return left or right

        return add(root,0,sum)
