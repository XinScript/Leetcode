# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(h,t):
            t_head = t_tail = None
            if h.next != t:
                t_tail,t_head = reverse(h.next,t)
                t_tail.next = h
            else:
                t_head = h
            return (h,t_head)
        
        h = t = head
        count = k
        rt = rh = None
        while(t):
            t = t.next
            count-=1
            if count == 0:
                b_tail,b_head = reverse(h,t)
                if not rt and not rh:
                    rt,rh = b_tail,b_head
                else:
                    rt.next = b_head
                    rt = b_tail
                b_tail.next = t
                h = t
                count = k
        return rh if rh else head

def c(l):
    a = []
    for i in range(len(l)):
        a.append(ListNode(l[i]))
    b = a[1:]
    h = p = a[0]
    while b:
        p.next = b.pop(0)
        p = p.next
    return h

def p(h):
    c = h
    while c:
        print(c.val)
        c = c.next


h = c([1, 2, 3, 4, 5])
# p(h)
n = Solution().reverseKGroup(h,6)
p(n)


            
            
