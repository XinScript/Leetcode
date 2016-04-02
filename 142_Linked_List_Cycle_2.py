# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def findIndex():
            if head is None:
                return None
            else:
                fast = head
                slow = head
                while fast and slow:
                    fast = fast.next
                    if fast is None:
                        return None
                    else:
                        fast = fast.next
                        slow = slow.next
                        if fast is slow:
                            return fast
                return None

        index = findIndex()

        if index:
            p1 = head
            p2 = index
            while p1 is not p2:
                p1 = p1.next
                p2 = p2.next
            return p1
        else:
            return None

