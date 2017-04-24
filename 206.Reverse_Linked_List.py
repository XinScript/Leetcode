# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        if head.next is None:
            return head
        else:
            t = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return t


    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        elif head.next is None:
            return head
        else:
            before = None
            while head:
                temp = head
                head = head.next
                temp.next = before
                before = temp
        return before
