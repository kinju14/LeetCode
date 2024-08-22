class Solution:
    def findComplement(self, num: int) -> int:
        d = {'0': '1', '1': '0'}
        s = bin(num).replace('0b','')
        res = ''.join(d[x] for x in s)
        return int(res,2)
