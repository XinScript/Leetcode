# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        def toRoot(root,s):
            if root is None:
                return
            if root.left is None and root.right is None:
                result.append(s+"->"+str(root.val))
            else:
                toRoot(root.left,s+"->"+str(root.val))
                toRoot(root.right,s+"->"+str(root.val))
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [str(root.val)]
        else:
            result = []
            toRoot(root.left,str(root.val))
            toRoot(root.right,str(root.val))

        return result

