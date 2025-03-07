#2523. Closest Prime Numbers in Range
class Solution:
    def closestPrimes(self, left, right):
        isPrime = self.sieveEratosthenes(right + 1)
        primes = [i for i in range(left, right + 1) if isPrime[i]]

        if len(primes) < 2:
            return [-1, -1]

        minDiff = float('inf')
        num1, num2 = -1, -1

        for a, b in zip(primes, primes[1:]):
            diff = b - a
            if diff < minDiff:
                minDiff = diff
                num1, num2 = a, b

        return [num1, num2] 

    def sieveEratosthenes(self, n):  
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False
        return isPrime 

