class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def getPrimes():
            isPrime = [True] * (right+1)
            isPrime[0] = isPrime[1] = False

            for n in range(2, int(sqrt(right)) + 1):
                if not isPrime[n]:
                    continue
                for m in range(n+n, right+1, n):
                    isPrime[m] = False

            primes = []
            for i in range(len(isPrime)):
                if isPrime[i] and i >= left:
                    primes.append(i)

            return primes

        primes = getPrimes()
        result = [-1, -1]
        diff = float('inf')

        for i in range(1, len(primes)):
            if primes[i] - primes[i-1] < diff:
                result = [primes[i-1], primes[i]]
                diff = primes[i] - primes[i-1]
        return result
