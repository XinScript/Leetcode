# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isSymmetric1(self, root):
        def isSym(p, q):
            if p is None and q is None:
                return True

            elif p is not None and q is not None:
                if p.val == q.val:
                    return isSym(p.left, q.right) and isSym(p.right, q.left)
                else:
                    return False
            else:
                return False
        if root is None:
            return True
        else:
            return isSym(root.left,root.right)


    def isSymmetric2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            stack1 = []
            stack2 = []
            node1 = node2 = root
            status = True
            while status:
                while node1 and node2:
                    if node1.val == node2.val:
                        stack1.append(node1)
                        stack2.append(node2)
                        node1 = node1.left
                        node2 = node2.right
                    else:
                        status = False
                        break
                else:
                    if not (node1 is None and node2 is None):
                        status = False
                        break
                    if len(stack1) > 0:
                        node1 = stack1.pop()
                        node2 = stack2.pop()
                        node1 = node1.right
                        node2 = node2.left
                    else:
                        break
            return status

