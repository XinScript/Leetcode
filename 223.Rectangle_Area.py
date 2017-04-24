class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area = (C-A)*(D-B)+(G-E)*(H-F)
        extra = 0
        if E<C<=G:
            if B<H<=D:
                extra = (C-max(A,E))*(H-max(B,F))
            elif F<D<=H:
                extra = (C-max(A,E))*(D-max(B,F))

        if A<G<=C:
            if B<H<=D:
                extra = (G-max(A,E))*(H-max(B,F))
            elif F<D<=H:
                extra = (G-max(A,E))*(D-max(B,F))

        return area-extra


print(Solution().computeArea(-2,-2,2,2,-3,1,-1,3))