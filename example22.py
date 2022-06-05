from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2:[int]) -> float:
        a,b = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        N,M = len(a), len(b)

        total_len = N + M

        num_to_make = (total_len + 1)//2

        lo = 0
        hi = min(N, num_to_make)


        while lo <hi:
            n = (lo + hi)//2
            m = num_to_make - n
            if m >0 and b[m -1] > a[n]:
                lo = n + 1
            else:
                hi = n
            

        n = lo
        m = num_to_make - n

        curr = a[n-1] if m == 0 or n >  0 and a[n-1] >= b[m -1] else [ m-1]

        if total_len % 2:
            return curr


        nxt = a[n] if m == M or n < N and a[n] <=b[m] else b[m]
        
        return (curr + next ) /2

        