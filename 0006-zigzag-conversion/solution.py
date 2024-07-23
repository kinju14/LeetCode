class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = defaultdict(str)

        n = len(s)
        i = 0
        x = numRows * 2 - 2
        for i in range(n):
            idx = i % x
            if idx < numRows:
                result[idx] += s[i]
            else:
                result[x - idx] += s[i]

        return ''.join(result.values())


        

