class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = ''
        count =  0
        charSet = ['a', 'b', 'c']

        def backtrack(string: str, curr_ch: str):
            nonlocal count
            if len(string) == n:
                count += 1
                if count == k:
                    return string
                else:
                    return ''

            for ch in charSet:
                if ch == curr_ch:
                    continue

                st = backtrack(string + ch, ch)
                if st:
                    return st

            return ''

        result = backtrack('', '')
        return result
        
            
        
