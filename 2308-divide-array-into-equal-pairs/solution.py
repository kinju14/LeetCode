class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        countArr = Counter(nums)
        count = 0
        for x in countArr.keys():
            count += 1 if (countArr[x] % 2) else 0
            if count > 1:
                return False

        return True
