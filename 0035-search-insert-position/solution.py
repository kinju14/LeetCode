class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i, j =0, n-1
        print(i, j)
        while i <= j:
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                j = mid - 1
            else:
                i = mid + 1

        return i
