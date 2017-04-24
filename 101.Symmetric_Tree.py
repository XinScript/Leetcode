# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            result = []
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

            node = root
            status = True
            i = 0
            while status:
                while node:
                    if result[i] == node.val:
                        i+=1
                        stack.append(node)
                        node = node.right
                    else:
                        status = False
                        break

                else:
                    if len(stack)!=0:
                        node = stack.pop()
                        node = node.left
                    else:
                        break

            return status



    @staticmethod
    def isSame(r1,r2):
        if r1 is None and r2 is None:
            return True
        elif r1 is None or r2 is None:
            return False
        elif r1.val == r2.val:
            return True
        else:
            return False