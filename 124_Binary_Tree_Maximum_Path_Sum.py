# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def findMax(root):
            if root.left and root.right:
                left = findMax(root.left)
                right = findMax(root.right)
                bigger = max(left, right)

                maxNum[0] = max(bigger,left+right+root.val,bigger+root.val,maxNum[0])
                return max(bigger + root.val,root.val)

            elif root.left:
                left = findMax(root.left)
                maxNum[0] = max(left,left+root.val,maxNum[0])
                return max(root.val,left+root.val)

            elif root.right:
                right = findMax(root.right)
                maxNum[0] = max(right,right+root.val,maxNum[0])
                return max(root.val,right+root.val)
            else:
                maxNum[0] = max(maxNum[0],root.val)
                return root.val


        if root:
            maxNum = [root.val]
            temp = findMax(root)
            return max(maxNum[0],temp)


