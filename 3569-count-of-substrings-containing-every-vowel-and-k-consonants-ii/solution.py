class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atleastk(k):
            count = defaultdict(int)
            res = 0
            l, cons = 0, 0

            for r in range(len(word)):
                if word[r] in 'aeiou':
                    count[word[r]] += 1
                
                else:
                    cons += 1
                
                while len(count) == 5 and cons >= k:
                    res += (len(word) - r)
                    if word[l] in 'aeiou':
                        count[word[l]] -= 1
                        if count[word[l]] == 0:
                            count.pop(word[l])
                    else:
                        cons -= 1
                    l += 1
            return res

        return atleastk(k) - atleastk(k + 1)
