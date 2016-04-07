#Sunday Algorithm
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle)>len(haystack):
            return -1
        else:
            subSize = len(needle)
            maxSize = len(haystack)
            index = 0
            while index+subSize<=maxSize:
                subIndex = 0
                while subIndex<subSize:
                    if needle[subIndex]!=haystack[index+subIndex]:
                        break
                    subIndex+=1
                if subIndex == subSize:
                    return index
                else:
                    new = index+subSize
                    if new < maxSize:
                        drift = 1
                        while drift<=subSize:
                            if needle[subSize-drift] == haystack[new]:
                                break
                            drift+=1
                        index+=drift
                    else:
                        return -1

            return -1

print(Solution().strStr("mississippi","pi"))




