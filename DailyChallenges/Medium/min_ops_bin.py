#3191. Minimum Operations to Make Binary Array Elements Equal to One I
def minOperations(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)-2):
            if nums[i]==0:
                nums[i+1]^=1
                nums[i+2]^=1
                ans+=1
        return -1 if nums[-1]==0 or nums[-2] ==0 else ans