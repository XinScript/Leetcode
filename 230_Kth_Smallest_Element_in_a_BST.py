# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def getSize(root, k):
            if root is None:
                return 0
            else:
                root.leftNum = getSize(root.left, k)
                root.rightNum = getSize(root.right, k)
                return root.leftNum + root.rightNum + 1

        size = getSize(root, k)
        while root:
            if k <= root.leftNum:
                root = root.left
            elif k == root.leftNum + 1:
                return root.val
            else:
                k = k - root.leftNum -1
                root = root.right
