class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.quene = []
        self.flag = True

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if x is None:
            return
        else:
            if self.flag:
                self.stack.append(x)
            else:
                while self.quene:
                    self.stack.append(self.quene.pop())
                self.flag = True
                self.stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        l = len(self.stack) + len(self.quene)
        if l > 0:
            if not self.flag:
                return self.quene.pop()
            else:
                i = 0
                while i < l:
                    self.quene.append(self.stack.pop())
                    i+=1
                self.flag = False
                return self.quene.pop()

    def peek(self):
        """
        :rtype: int
        """
        l = len(self.stack) + len(self.quene)
        if l > 0:
            if self.flag:
                return self.stack[0]
            else:
                return self.quene[l-1]

    def empty(self):
        """
        :rtype: bool
        """
        l = len(self.stack)+len(self.quene)
        print(l)
        if l > 0:
            return False
        else:
            return True


q = Queue()
print(q.empty())
q.push(1)
q.push(2)
q.pop()
q.push(3)
q.push(4)
q.push(5)
q.pop()
q.pop()
print(q.quene)