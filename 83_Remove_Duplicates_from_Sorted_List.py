# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        else:
            node = head.next
            before = head
            while node:
                while before.val == node.val:
                    node = node.next
                    if node is None:
                        before.next = None
                        break
                else:
                    if before.next is not node:
                        before.next = node
                    before = node
                    node = node.next

            return head


