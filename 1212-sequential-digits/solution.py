class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        string = '123456789'

        start = len(str(low))
        end = len(str(high))

        for length in range(start, end+1):
            l = 0
            r = l+length
            while r < 10:
                num = int(string[l:r])
                if num >= low and num <= high:
                    res.append(num)
                r += 1
                l += 1

        return res
        
