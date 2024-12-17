## Product of Array Except Self

def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=[0]*n
        right=[0]*n
        f,r=1,1
        left[0]=1
        right[n-1]=1
        if len(nums)==1:
            return 1
        for i in range(1,n):
            f*=nums[i-1]
            left[i]=f
        for j in range(n-2,-1,-1):
            r*=nums[j+1]
            right[j]=r
        for k in range(n):
            nums[k]=left[k]*right[k]
        return nums
