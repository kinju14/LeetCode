class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True

        d = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                d.append([s1[i], s2[i]])

            if len(d) > 2: 
                return False
        
        
        if len(d) == 2 and d[0][0] == d[1][1] and d[0][1] == d[1][0] : return True 
        else: return False

        
