# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA and headB:
            p1 = headA
            p2 = headB
            count1 = 0
            count2 = 0
            while p1:
                p1=p1.next
                count1+=1
            while p2:
                p2=p2.next
                count2+=1
            p1 = headA
            p2 = headB

            if count1>count2:
                gap = count1-count2
                while gap:
                    p1 = p1.next
                    gap-=1
            else:
                gap = count2-count1
                while gap:
                    p2 = p2.next
                    gap-=1

            while p1 and p2:
                if p1 is p2:
                    return p1
                else:
                    p1 = p1.next
                    p2 = p2.next



