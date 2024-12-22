def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    arr=[]
    def f(ind,l,target,arr):
        if target<0:
            return
        if target==0:
            arr.append(l)
            return
        for i in range(ind,len(candidates)):
            if i>ind and candidates[i]==candidates[i-1]:
                continue
            if target<candidates[i]:
                break
            f(i+1,l+[candidates[i]],target-candidates[i],arr)
    f(0,[],target,arr)
    return arr