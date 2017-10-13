class Solution(object):
  def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    arr = ''
    l = 0
    for i in s:
	    	index = arr.find(i)
	    	if index > -1:
    			arr = arr[index+1:]+i
    		else:
    			arr+=i
    			l = max(l,len(arr))
    return l
