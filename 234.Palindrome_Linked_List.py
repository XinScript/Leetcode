# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        elif head.next is None:
            return True
        else:
            p = head
            size = 0
            while p:
                size+=1
                p = p.next
            if size%2 == 0:
                isEven = True
            else:
                isEven = False

            p = head
            before = None
            for i in range(0,size//2):
                temp = p
                p = p.next
                temp.next = before
                before = temp
            if isEven:
                while p:
                    if p.val != before.val:
                        return False
                    else:
                        p = p.next
                        before = before.next

            else:
                p = p.next
                while p:
                    if p.val != before.val:
                        return False
                    else:
                        p = p.next
                        before = before.next
            return True


def makeLink(node,arg):
    for i in arg:
        node.next = ListNode(i)
        node = node.next

def printList(node):
    while node:
        print(node.val)
        node = node.next
head = ListNode(1)
# makeLink(head,[1])
printList(head)
print(Solution().isPalindrome(head))
