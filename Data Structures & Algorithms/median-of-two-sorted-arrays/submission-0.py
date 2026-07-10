class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = nums1 + nums2
        combined.sort()
        midpoint = int((len(combined) - 1) / 2)
        if len(combined) % 2 == 1:
            return combined[midpoint]
        else:
            return (combined[midpoint] + combined[midpoint+1]) / 2