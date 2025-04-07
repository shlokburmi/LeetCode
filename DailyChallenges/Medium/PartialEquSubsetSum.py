#416. Partition Equal Subset Sum
def canPartition(self, nums: List[int]) -> bool:
        total_sum, remainder = divmod(sum(nums), 2)
        if remainder:
            return False
        can_partition = [True] + [False] * total_sum
        for num in nums:
            for j in range(total_sum, num - 1, -1):
                can_partition[j] = can_partition[j] or can_partition[j - num]
        return can_partition[total_sum]