class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = dict(zip(heights, names))
        d = dict(sorted(d.items(), reverse=True))

        return d.values()

        
