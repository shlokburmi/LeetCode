#2818. Apply Operations to Maximize Score

MOD = 1_000_000_007  # Class-level constant

def maximumScore(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = 1
        minPrimeFactors = self._sieveEratosthenes(max(nums) + 1)
        primeScores = [self._getPrimeScore(num, minPrimeFactors) for num in nums]

        left = [-1] * n
        right = [n] * n
        stack = []

        # Find left limits
        for i in reversed(range(n)):
            while stack and primeScores[stack[-1]] <= primeScores[i]:
                left[stack.pop()] = i
            stack.append(i)

        stack = []

        # Find right limits
        for i in range(n):
            while stack and primeScores[stack[-1]] < primeScores[i]:
                right[stack.pop()] = i
            stack.append(i)

        numAndIndexes = [(num, i) for i, num in enumerate(nums)]

        def modPow(x: int, n: int) -> int:
            if n == 0:
                return 1
            if n % 2 == 1:
                return x * modPow(x, n - 1) % self.MOD
            return modPow(x * x % self.MOD, n // 2)

        for num, i in sorted(numAndIndexes, key=lambda x: (-x[0], x[1])):
            rangeCount = (i - left[i]) * (right[i] - i)
            actualCount = min(rangeCount, k)
            k -= actualCount
            ans *= modPow(num, actualCount)
            ans %= self.MOD

        return ans

def _sieveEratosthenes(self, n: int) -> list[int]:
        """Gets the minimum prime factor of i, where 2 <= i <= n."""
        minPrimeFactors = [i for i in range(n + 1)]
        for i in range(2, int(n**0.5) + 1):
            if minPrimeFactors[i] == i:  # `i` is prime.
                for j in range(i * i, n, i):
                    minPrimeFactors[j] = min(minPrimeFactors[j], i)
        return minPrimeFactors

def _getPrimeScore(self, num: int, minPrimeFactors: list[int]) -> int:
        primeFactors = set()
        while num > 1:
            divisor = minPrimeFactors[num]
            primeFactors.add(divisor)
            while num % divisor == 0:
                num //= divisor
        return len(primeFactors)