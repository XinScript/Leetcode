class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        a = list(a)
        b = list(b)
        flag = False

        while a and b:
            if flag:
                r = int(a.pop()) + int(b.pop()) + 1
            else:
                r = int(a.pop()) + int(b.pop())
            if r >1:
                flag = True
                result = str(r-2) + result
            else:
                result = str(r) + result
                flag = False
        while a:
            if flag:
                r = int(a.pop()) + 1
            else:
                r = int(a.pop())

            if r == 2:
                flag = True
                result = str(r-2) + result
            else:
                flag = False
                result = str(r) + result

        while b:
            if flag:
                r = int(b.pop()) + 1
            else:
                r = int(b.pop())
            if r == 2:
                flag = True
                result = str(r-2) + result
            else:
                flag = False
                result = str(r) + result

        if flag:
            result = "1" + result

        return result


# print(Solution().addBinary("1111", "1111"))
