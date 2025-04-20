class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total = 0
        
        for answer, freq in count.items():
            group_size = answer + 1
            groups_needed = math.ceil(freq / group_size)
            total += groups_needed * group_size
        
        return total
