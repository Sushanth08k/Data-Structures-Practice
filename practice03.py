## Subsets using Recursion
def subset(i,l,n):
    if i>=n:
        res.append(l[:])
        return
    l.append(nums[i])
    subset(i+1,l,n)
    l.pop()
    subset(i+1,l,n)
nums=[1,2,3]
n=len(nums)
l=[]
res=[]
i=0
subset(i,l,n)
print(res)