# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None

        node1 = head
        node2 = head

        while n:
            node2 = node2.next
            n-=1
        if node2 is None:
            return node1.next
        before = None
        while node2:
            before = node1
            node1 = node1.next
            node2 = node2.next
        before.next = node1.next
        return head

