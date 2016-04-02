# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root is None:
            return result
        else:
            stack = []
            node = root
            while True:
                while node:
                        result.append(node.val)
                        stack.append(node)
                        node = node.left
                else:
                    if len(stack)!=0:
                        node = stack.pop()
                        node = node.right
                    else:
                        break
        return result
