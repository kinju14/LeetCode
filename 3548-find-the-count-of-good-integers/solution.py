class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        def count_permutations(s):
            counter = Counter(s)
            total = factorial(len(s))
            for freq in counter.values():
                total //= factorial(freq)
            
            # Remove permutations with leading zero
            if counter['0'] > 0:
                counter['0'] -= 1
                total_with_leading_zero = factorial(len(s) - 1)
                for freq in counter.values():
                    total_with_leading_zero //= factorial(freq)
                total -= total_with_leading_zero
                counter['0'] += 1
            return total

        seen = set()
        res = 0

        half = (n + 1) // 2
        start = 10 ** (half - 1)
        end = 10 ** half

        for first_half in range(start, end):
            s = str(first_half)
            full = s + s[-2::-1] if n % 2 else s + s[::-1]
            if full[0] == '0':
                continue
            num = int(full)
            if num % k == 0:
                key = tuple(sorted(full))
                if key not in seen:
                    seen.add(key)
                    res += count_permutations(full)

        return res
