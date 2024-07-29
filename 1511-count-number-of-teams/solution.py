class Solution:
    def numTeams(self, rating: List[int]) -> int:
        result = 0
        n = len(rating)

        for i in range(n):
            leftSmaller, rightLarger, leftLarger, rightSmaller = 0, 0, 0, 0

            for left in range(i-1, -1, -1):
                if rating[left] < rating[i]:
                    leftSmaller += 1
                else:
                    leftLarger += 1
                
            for right in range(i+1, n):
                if rating[i] < rating[right]:
                    rightLarger += 1
                else:
                    rightSmaller += 1

            result += (leftSmaller * rightLarger) + (leftLarger * rightSmaller)
            
        return result
