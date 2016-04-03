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


l1 = ListNode(2)
# l2 = ListNode(2)
# l3 = ListNode(2)
# l4 = ListNode(2)
# l5 = ListNode(5)
# l6 = ListNode(6)
# l1.next = l2
# l2.next = l3
# l3.next = l4
# l4.next = l5
# l5.next = l6
r = Solution().deleteDuplicates(l1)
while r:
    print(r.val)
    r = r.next