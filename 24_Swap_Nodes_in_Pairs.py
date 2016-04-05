# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head

        p1 = head1  = head
        p2 = head2 = head.next
        while p2:
            p1.next = p1.next.next
            if p2.next:
                p2.next = p2.next.next
            p2 = p2.next
            p1 = p1.next

        p1 = head1
        p2 = head2

        while p2:
            temp = p2
            p2 = p2.next
            temp.next = p1
            if p2 is None:
                break
            temp2 = p1
            p1 = p1.next
            temp2.next = p2

        return head2
