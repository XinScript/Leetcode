# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        elif head.next is None:
            return head
        else:
            head2 = p1 = head.next
            before = head
            count = False
            while p1.next is not None:
                before.next = p1.next
                before=p1
                p1 = p1.next
                count = not count
            if count:
                before.next = None
                p1.next = head2
            else:
                before.next = head2


        return head
