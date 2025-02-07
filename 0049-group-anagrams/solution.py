class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        
        for s in strs:
            a = [0]* 26
            for ch in s:
                a[ord(ch) - ord('a')] += 1
            output[tuple(a)].append(s)

        return list(output.values())

        

