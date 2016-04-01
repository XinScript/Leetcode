class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = []
        index = 0
        divider = 2**index
        i = 0
        while i <= num:
            if i == 0:
                result.append(0)
            else:
                result.append(result[i%divider]+1)
                if i == divider*2-1:
                    index+=1
                    divider = 2**index

            i+=1

        return result


