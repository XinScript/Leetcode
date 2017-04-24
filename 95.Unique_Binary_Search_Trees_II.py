# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def gt(nums):
            if nums:
                if len(nums) == 1:
                    return [TreeNode(nums[0])]
                i = 0
                temp = []
                while i < len(nums):
                    if i == 0:
                        right = gt(nums[i+1:])
                        for j in right:
                            root = TreeNode(nums[i])
                            root.right = j
                            temp.append(root)
                    elif i == len(nums)-1:
                        left = gt(nums[:i])
                        for j in left:
                            root = TreeNode(nums[i])
                            root.left = j
                            temp.append(root)
                    else:
                        left = gt(nums[:i])
                        right = gt(nums[i+1:])
                        for j1 in left:
                            for j2 in right:
                                root = TreeNode(nums[i])
                                root.left = j1
                                root.right = j2
                                temp.append(root)

                    i+=1
                return temp

            else:
                return []

        nums = [i for i in range(1,n+1)]

        return gt(nums)

result = Solution().generateTrees(3)

def printTree(root):
    if root is None:
        return
    else:
        printTree(root.left)
        print(root.val)
        printTree(root.right)

for i in result:
    printTree(i)
    print("")
