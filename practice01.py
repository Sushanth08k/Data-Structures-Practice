#CircularArrayLoop
def circularArrayLoop(self, nums: List[int]) -> bool:
        def getnext(x):
            return (x+nums[x])%len(nums)
        for i in range(len(nums)):
            slow,fast=i,getnext(i)
            while True:
                if slow==getnext(slow) or  fast==getnext(fast):
                    break
                if nums[slow]*nums[getnext(slow)]<0 or nums[fast]*nums[getnext(fast)]<0:
                    break
                slow,fast=getnext(slow),getnext(getnext(fast))
                if slow ==fast:
                    return True
        return False