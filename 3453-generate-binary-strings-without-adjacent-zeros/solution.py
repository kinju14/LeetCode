class Solution:
    def validStrings(self, n: int) -> List[str]:
        l = []
        s = ''
        def rec(s: string):
            if len(s) == n:
                l.append(s)
                return
            if s[-1] == '0':
                rec(s+'1')
            else:
                rec(s+'0')
                rec(s+'1')

        rec(s+'0')
        rec(s+'1')
        return l
