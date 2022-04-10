class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c = nums1 + nums2
        c.sort()
        a = len(c)
        d=0
        if a%2==0:
            d=(c[int(a/2)-1]+c[int(a/2)])/2
        else:
            d = c[a//2]
        return d