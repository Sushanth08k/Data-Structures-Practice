#3SumClosest
def threeSumClosest(self, nums: List[int], target: int) -> int:
    n=len(nums)
    nums.sort()
    l=[]
    closest = float('inf')
    for i in range(len(nums)):
        j=i+1
        k=n-1
        while j<k:
            m=nums[i]+nums[j]+nums[k]
            if abs(target - m) < abs(target - closest):
                closest = m
            if m==target:
                return m 
            elif m>target:
                k-=1
            else:
                j+=1
    return closest

#Input: nums = [-1,2,1,-4], target = 1
#Output: 2
#Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
