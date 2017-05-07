# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        stack = []
        while head:
        	stack.append(head.val)
        	head = head.next

        def construct(arr):
        	if not arr:
        		return None
        	midpoint = int((len(arr)-1)/2)
        	node = TreeNode(arr[midpoint])
        	left = construct(arr[:midpoint])
        	right = construct(arr[midpoint+1:])
        	node.left = left
        	node.right = right
        	return node

        return construct(stack)

