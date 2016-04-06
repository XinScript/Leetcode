class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        if self.q1:
            self.q1.pop()

        self.q1,self.q2 = self.q2,self.q1

    def top(self):
        """
        :rtype: int
        """
        if self.q1:
            return self.q1[-1]


    def empty(self):
        """
        :rtype: bool
        """
        if self.q1:
            return False
        else:
            return True