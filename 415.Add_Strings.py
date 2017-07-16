class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        gap = abs(len(num1)-len(num2))
        prefix = ''.join('0' for i in range(gap))
        if len(num1)>len(num2):
        	num2 = prefix + num2
        else:
        	num1 = prefix + num1

        results = ''

        flag = False

        i = len(num1)-1

        while i >= 0:
        	a = int(num1[i])
        	b = int(num2[i])
        	s = a+b
        	if flag:
        		s+=1
        	if s>=10:
        		flag = True
        		s-=10
        	else:
        		flag = False
        	results = str(s)+results
        	i-=1
        if flag:
        	results = '1'+results
        return results

Solution().addStrings('23','85')


