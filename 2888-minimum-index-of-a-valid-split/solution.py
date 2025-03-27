class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freqMap = Counter(nums)
        maxEl = freqMap.most_common(1)[0][0]
        n = len(nums)
        lCount = 0
        rCount = freqMap[maxEl]

        for i in range(n):
            if nums[i] == maxEl:
                lCount += 1
                rCount -= 1

            if lCount * 2 > i+1 and rCount * 2 > n-i-1:
                return i
        return -1
            
