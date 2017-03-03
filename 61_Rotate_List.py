# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        length = 0
        my_head = head
        tail = None
        while(my_head):
            length+=1
            if my_head.next is None:
                tail = my_head
            my_head = my_head.next
        tail.next = head
        remain = k % length
        complement = length - remain
        my_head = head
        for i in range(complement-1):
            my_head = my_head.next
        new_head = my_head.next
        my_head.next = None
        return new_head
