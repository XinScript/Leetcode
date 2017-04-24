class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        s1 = version1.split(".")
        s2 = version2.split(".")
        l1 = len(s1)
        l2 = len(s2)
        size = max(l1,l2)
        for i in range(0,size):
            if i < l2:
                b = int(s2[i])
            else:
                b = 0
            if i < l1:
                a = int(s1[i])
            else:
                a = 0
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0

