#Problem-2460
def applyOperations(self, nums):
        ans=[0]*len(nums)
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        j=0
        for num in nums:
            if num>0:
                ans[j]=num
                j+=1
        return ans