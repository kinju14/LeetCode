from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(set(word)) <= 8:
            return len(word)
        count = sorted(Counter(word).items(), key = lambda x: x[1], reverse = True)

        i = 0
        result = 0

        for (k, v) in count:
            result += v * ((i // 8) + 1)
            i += 1

        return result
