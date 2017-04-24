# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        def find(root,nums):
            if root is None:
                return []
            else:
                if root.left and root.right:
                    find(root.left,nums+[root.val])
                    find(root.right,nums+[root.val])
                elif root.left:
                    find(root.left,nums+[root.val])
                elif root.right:
                    find(root.right,nums+[root.val])
                else:
                    s = nums+[root.val]
                    r = 0
                    for i in s:
                        r+=i
                    if r == sum:
                        result.append(s)

        find(root,[])

        return result




