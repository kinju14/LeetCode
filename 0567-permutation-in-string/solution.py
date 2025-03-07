class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        chars1, chars2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            chars1[ord(s1[i]) - ord('a')] += 1
            chars2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if chars1[i] == chars2[i] else 0)

        l = 0
        r = len(s1)

        while r < len(s2):
            if matches == 26:
                return True

            idx = ord(s2[r]) - ord('a')
            chars2[idx] += 1
            if chars2[idx] == chars1[idx]:
                matches += 1
            elif chars2[idx] == chars1[idx] + 1:
                matches -= 1

            idx = ord(s2[l]) - ord('a')
            chars2[idx] -= 1
            if chars2[idx] == chars1[idx]:
                matches += 1
            elif chars2[idx] == chars1[idx] - 1:
                matches -= 1

            r += 1
            l += 1
        
        return matches == 26
