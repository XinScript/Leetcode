class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<10:
            return n
        offset,num,remain=1,1,n
        while offset*num*9<n:
            remain = remain-(offset)*9*num
            offset,num = offset+1,num*10
        div,remain = divmod(remain,offset)
        result = str(num+div)[remain-1] if remain else str(num+div-1)[-1]
        return int(result)
