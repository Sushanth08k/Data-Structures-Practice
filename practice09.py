def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    def f(ind,l,res):
        res.append(l[:])
        for i in range(ind,n):
            if i!=ind and nums[i]==nums[i-1]:
                continue
            f(i+1,l+[nums[i]],res)
    res=[]
    nums.sort()
    n=len(nums)
    f(0,[],res)
    return res
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]