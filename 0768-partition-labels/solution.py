class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = defaultdict(int)
        res = []

        for i in range(len(s)):
            lastIdx[s[i]] = i
        i = 0
        while i < len(s):
            start = i
            end = lastIdx[s[i]]
            while start < end+1:
                if lastIdx[s[start]] > end:
                    end = lastIdx[s[start]]
                start += 1
            res.append(end-i+1)
            i = end+1

        return res
