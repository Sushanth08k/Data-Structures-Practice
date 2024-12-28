def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        def f(h,n,target):
            if target<=0 or target>(n*k):
                return 0
            if n==1:
                return 1
            if (n,target) in h:
                return h[(n,target)]
            res=0
            for i in range(1,k+1):
                res+=f(h,n-1,target-i)
            h[(n,target)]=res
            return h[(n,target)]
        h={}
        return f(h,n,target) % (10 ** 9 + 7)