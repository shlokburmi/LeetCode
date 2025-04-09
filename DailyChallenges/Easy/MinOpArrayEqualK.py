#3375. Minimum Operations to Make Array Values Equal to K
  def minOperations(self, nums: list[int], k: int) -> int:
    numsSet = set(nums)
    mn = min(nums)
    if mn < k:
      return -1
    if mn > k:
      return len(numsSet)
    return len(numsSet) - 1