# Combination Sum using recursion
def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def f(ind,l,targ,res):
            if ind==len(candidates):
                if target==0:
                    res.append(l)
                return
            if candidates[ind]<=target:
                l.append(candidates[ind])
                f(ind,l,target-candidates[ind],res)
                l.pop()
            f(ind+1,l,target,res)
        f(0,[],target,[])
        return res