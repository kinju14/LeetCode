class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        count = defaultdict(int)
        count[0] = 1  # Start with prefix sum 0
        prefix_sum = 0
        result = 0

        for num in nums:
            # Treat element as 1 if num % modulo == k, else 0
            if num % modulo == k:
                prefix_sum += 1
            
            # Look for previous prefix sums that satisfy the condition
            needed = (prefix_sum - k) % modulo
            result += count[needed]

            # Update the map
            count[prefix_sum % modulo] += 1

        return result
