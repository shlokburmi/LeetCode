#2529. Maximum Count of Positive Integer and Negative Integer
def maximumCount(self, nums):
         return max(sum(num>0 for num in nums),sum(num <0 for num in nums))   