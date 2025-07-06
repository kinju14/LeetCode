from collections import Counter

class FindSumPairs:
    def __init__(self, nums1, nums2):
        self.arr1 = nums1
        self.arr2 = nums2
        self.freq = Counter(nums2)

    def add(self, index, val):
        old_val = self.arr2[index]
        self.freq[old_val] -= 1
        self.arr2[index] += val
        new_val = self.arr2[index]
        self.freq[new_val] += 1

    def count(self, tot):
        total = 0
        for num in self.arr1:
            total += self.freq[tot - num]
        return total
