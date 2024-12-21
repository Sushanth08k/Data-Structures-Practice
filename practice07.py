def generateParenthesis(self, n: int) -> List[str]:
    def f(str1,open,close,arr):
        if len(str1)==2*n:
            print(str1)
            arr.append(str1)
            return
        if open<n:
            f(str1+"(",open+1,close,arr)
        if open>close:
            f(str1+")",open,close+1,arr)
    arr=[]
    f("",0,0,arr)
    return arr