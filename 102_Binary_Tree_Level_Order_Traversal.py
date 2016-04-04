# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        else:
            quene = [root]
            result = []
            currentNum = 1
            nextNum = 0
            while quene:
                current = []
                while currentNum > 0:
                    node = quene.pop(0)
                    current.append(node.val)
                    currentNum -= 1
                    if node.left:
                        quene.append(node.left)
                        nextNum+= 1
                    if node.right:
                        quene.append(node.right)
                        nextNum += 1
                result.append(current)
                currentNum=nextNum
                nextNum = 0
        return result
