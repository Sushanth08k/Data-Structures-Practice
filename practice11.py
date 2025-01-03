def letterCombinations(self, digits: str) -> List[str]:
    if not digits:
        return []
        
    d = {'2': 'abc','3': 'def','4': 'ghi','5': 'jkl','6': 'mno','7': 'pqrs','8': 'tuv','9': 'wxyz'}
    def f(ind,comb):
        if ind==len(digits):
            res.append(comb[:])
            return
        for i in d[digits[ind]]:
            f(ind+1,comb+i)
    res=[]
    f(0,"")
    return res