class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs.pop()

        result = ""
        start = strs[0]

        for i in range(1,len(strs)):
            if len(strs[i]) < len(start):
                start = strs[i]

        flag = False
        for i in range(0, len(start)):
            for s in strs:
                if s[i]!= start[i]:
                    flag = True
                    break
            if flag:
                break
            result = result + start[i]

        return result
