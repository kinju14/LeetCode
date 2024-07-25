class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums
        
        mid = n // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        merged = self.mergeArrays(left, right)

        return merged

    
    
    def mergeArrays(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i, j = 0, 0
        n1, n2 = len(arr1), len(arr2)
        result = []

        while i < n1 and j < n2:
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1

        result += arr1[i:]
        result += arr2[j:]

        return result
