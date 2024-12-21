# NEXT PERMUTATION
def nextPermutation(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    flag=False
    n=len(nums)
    for i in range(n-1,0,-1):
        if nums[i-1]<nums[i]:
            bp=i-1
            flag=True
            break
    if flag:
        mini=float('inf')
        for j in range(bp+1,n):
            if nums[j]>nums[bp] and nums[j]<=mini:
                mini=nums[j]
                minind=j
        nums[bp],nums[minind]=nums[minind],nums[bp]
        nums[bp+1:]=nums[bp+1:][::-1]
        return nums
    else:
        return nums.sort()