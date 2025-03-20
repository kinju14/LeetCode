class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False

        countChars = Counter(nums)

        for n in sorted(countChars):
            while countChars[n]:
                count = 1
                countChars[n] -= 1
                while count < k:
                    if not countChars[n+count]:
                        return False
                    countChars[n+count] -= 1
                    count += 1

        return True

