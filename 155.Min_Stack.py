class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        self.size = 0
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if self.size == 0 or x<=self.min[-1]:
            self.min.append(x)
        self.size+=1
    def pop(self):
        """
        :rtype: nothing
        """
        if self.size:
            top = self.stack.pop()
            self.size-=1
            if top == self.min[-1]:
                self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.size:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.size:
            return self.min[-1]
