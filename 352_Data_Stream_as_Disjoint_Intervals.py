# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = [];
        

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append(Interval(val,val))
        else:
            if val < self.stack[0].start:
                if self.stack[0].start-1==val:
                    self.stack[0].start = val
                else:
                    self.stack.insert(0,Interval(val,val))
            elif val > self.stack[-1].end:
                if self.stack[-1].end+1==val:
                    self.stack[-1].end = val
                else:
                    self.stack.append(Interval(val,val))
            else:
                for i in range(1,len(self.stack)):
                    if self.stack[i-1].end<val<self.stack[i].start:
                        if self.stack[i].start-self.stack[i-1].end==2:
                            new = Interval(self.stack[i-1].start,self.stack[i].end)
                            self.stack.pop(i)
                            self.stack.pop(i-1)
                            break
                        elif self.stack[i-1].end + 1 == val:
                            self.stack[i-1].end = val
                        elif self.stack[i].start - 1 == val:
                            self.stack[i].start = val
                        else:
                            self.stack.insert(i,Interval(val,val))



    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self.stack
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()