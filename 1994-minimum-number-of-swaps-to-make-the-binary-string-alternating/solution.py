class Solution:
    def minSwaps(self, s: str) -> int:
        count = Counter(s)

        if abs(count['0'] - count['1']) > 1:
            return -1
        
        def countSwaps(curr):
            mismatch = 0
            for i in range(len(s)):
                if int(s[i]) != curr:
                    mismatch += 1
                curr = not curr
            return mismatch // 2

        if count['0'] == count['1']:
            return min(countSwaps(0), countSwaps(1))

        curr = 1
        if count['0'] > count['1']:
            curr = 0
        
        return countSwaps(curr)


