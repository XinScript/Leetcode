# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            if l1.val < l2.val:
                node = head = l1
                l1 = l1.next
            else:
                node = head = l2
                l2 = l2.next

            while l1 and l2:
                if l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next

            if l1:
                node.next = l1
            if l2:
                node.next = l2

            return head



l1 = ListNode(1)
l3 = ListNode(3)
l5 = ListNode(5)
l1.next = l3
l3.next = l5

l2 = ListNode(2)
l4 = ListNode(4)

l2.next = l4

t = Solution().mergeTwoLists(l2,l1)

while t:
    print(t.val)
    t = t.next
