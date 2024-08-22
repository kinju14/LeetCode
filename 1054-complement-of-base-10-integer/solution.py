class Solution:
    def bitwiseComplement(self, n: int) -> int:
        d = {'0': '1', '1': '0'}
        s = bin(n).replace('0b','')
        res = ''.join(d[x] for x in s)
        return int(res,2)
