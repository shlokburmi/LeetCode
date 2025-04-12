#3272. Find the Count of Good Integers
def countGoodIntegers(self, n: int, k: int) -> int:
    halfLength = (n + 1) // 2
    minHalf = 10**(halfLength - 1)
    maxHalf = 10**halfLength
    ans = 0
    seen = set()
    for num in range(minHalf, maxHalf):
      palindrome = str(num) + str(num)[::-1][n % 2:]
      sortedDigits = ''.join(sorted(palindrome))
      if int(palindrome) % k != 0 or sortedDigits in seen:
        continue
      seen.add(sortedDigits)
      digitCount = collections.Counter(palindrome)
      firstDigitChoices = n - digitCount['0']
      permutations = firstDigitChoices * math.factorial(n - 1)
      for freq in digitCount.values():
        permutations //= math.factorial(freq)
      ans += permutations
    return ans