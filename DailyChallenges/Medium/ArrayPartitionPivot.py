#2161. Partition Array According to Given Pivot
def pivotArray(self, nums, pivot):
        return [num for num in nums if num<pivot]+[num for num in nums if num==pivot]+[num for num in nums if num>pivot]
