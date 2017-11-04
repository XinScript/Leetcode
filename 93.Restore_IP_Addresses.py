class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        rs = []
        def backtrack(string,count,dot_num,index):
        	if index == len(s):
        		if dot_num == 3 and int(string[-count:])<256:
        			rs.append(string)
        		return
        	if count == 0 or count == 2:
        		backtrack(string+s[index],count+1,dot_num,index+1)
        	if count == 1 and string[-1]!='0':
        		backtrack(string+s[index],count+1,dot_num,index+1)
        	if count>0 and dot_num<3 and int(string[-count:])<256:
        		backtrack(string+".",0,dot_num+1,index)
        	return 
        backtrack("",0,0,0)
        return rs
print(Solution().restoreIpAddresses("010010"))



