class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []

        i = 0
        while i < len(word) and word[i] != ch:
            i += 1
        print(i, stack)

        if i >= len(word):
            return word

        return word[:i+1][::-1] + word[i+1:]
