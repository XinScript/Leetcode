class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        a = {"}":"{","]":"[",")":"("}
        b = {"(","[","{"}
        for i in s:
            if i in b:
                stack.append(i)
            else:
                if len(stack)>0:
                    if stack.pop() != a[i]:
                        return False
                else:
                    return False
        if stack:
            return False
        return True





