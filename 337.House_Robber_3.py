# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def count(root):
            if root is None:
                return 0,0
            l1,l2 = count(root.left)
            r1,r2 = count(root.right)

            if root.val is None:
                used = r2+l2
            else:
                used = root.val+r2+l2

            notUsed = max(l1,l2)+max(r1,r2)

            return used,notUsed
        return max(count(root))


t1 = TreeNode(3)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(3)
t5 = TreeNode(1)
t1.left = t2
t2.right = t4
t1.right = t3
t3.right = t5
print(Solution().rob(t1))