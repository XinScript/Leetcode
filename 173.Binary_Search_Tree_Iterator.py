class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.current = None

        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if len(self.stack) else False

    def next(self):
        """
        :rtype: int
        """
        self.current = self.stack.pop()
        if self.current.right:
            node = self.current.right
            while node:
                self.stack.append(node)
                node = node.left
        return self.current.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())


