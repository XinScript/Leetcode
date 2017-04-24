class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num:
            result = ''
            temp = abs(num)
            while temp:
                temp,remainer = divmod(temp,7)
                result += str(remainer)
            result = result[::-1]
            return result if num >= 0 else "-"+result
        else:
            return '0'

print(divmod(-7,8))
