# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    result = []
    current_num = None
    count = 1
    max_count = 0
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        def handle_val(val):
            if self.current_num is None:
                self.current_num = val
            elif val == self.current_num:
                self.count+=1
            else:
                if self.count > self.max_count:
                    self.max_count = self.count
                    self.result = [self.current_num]
                elif self.count == self.max_count:
                        self.result.append(self.current_num)
                self.count = 1
                self.current_num = val

        def r(node):
            if node is None:
                return None
            left = r(node.left)
            handle_val(node.val)
            right = r(node.right)

        r(root)
        if self.count > self.max_count:
            self.max_count = self.count
            self.result = [self.current_num]
        elif self.count == self.max_count:
                self.result.append(self.current_num)
                
        return self.result
