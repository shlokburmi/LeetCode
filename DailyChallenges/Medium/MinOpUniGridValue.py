#2033. Minimum Operations to Make a Uni-Value Grid

def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = sorted([a for row in grid for a in row])
        if any((a - arr[0]) % x for a in arr):
            return -1
        ans = 0
        for a in arr:
            ans += abs(a - arr[len(arr) // 2]) // x
        return ans