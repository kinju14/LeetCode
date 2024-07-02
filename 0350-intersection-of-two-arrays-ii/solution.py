class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                temp.append(nums1[i])
                nums2.pop(nums2.index(nums1[i]))
        return temp
