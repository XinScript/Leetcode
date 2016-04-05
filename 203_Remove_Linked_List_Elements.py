# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        else:
            guard = ListNode(0)
            before = guard
            before.next = head
            node = head
            while node:
                if node.val == val:
                    before.next = node.next
                else:
                    before = node
                node = node.next
            return guard.next







