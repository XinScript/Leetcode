class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def findKth(a, b, k):
            m = len(a)
            n = len(b)
            if m > n:
                return findKth(b, a,k)
            elif m == 0:
                return b[k-1]
            elif k == 1:
            	return min(a[0],b[0])
            pa = min(k//2,m) 
            pb = k - pa
            if a[pa-1] < b[pb-1]:
            	return findKth(a[pa:],b,k-pa)
            elif a[pa-1] > b[pb-1]:
            	return findKth(a,b[pb:],k-pb)
            else:
            	return b[pb-1]

        total = len(nums1)+len(nums2)
        return findKth(nums1, nums2, total//2+1) if total % 2 else (findKth(nums1, nums2, total//2)+findKth(nums1, nums2, total//2+1))/2







