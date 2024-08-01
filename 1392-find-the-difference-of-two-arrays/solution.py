class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l1 = set(nums1)
        l2 = set(nums2)
        return [list(l1.difference(l2)), list(l2.difference(l1))]
