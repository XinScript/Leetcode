# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        else:
            fast = head
            slow = head
            while fast and slow:
                fast = fast.next
                if fast is None:
                    return False
                else:
                    fast = fast.next
                    slow = slow.next
                    if fast is slow:
                        return True
            return False
