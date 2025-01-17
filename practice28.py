# 2657. Find the Prefix Common Array of Two Arrays
# Input: A = [1,3,2,4], B = [3,1,2,4]
# Output: [0,2,3,4]
# Explanation: At i = 0: no number is common, so C[0] = 0.
# At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
# At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
# At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        n=len(A)
        c=[0]*n
        cnt=0
        hash1=set()
        for i in range(n):
            if B[i] in hash1:
                cnt+=1
            hash1.add(B[i])
            if A[i] in hash1:
                cnt+=1
            hash1.add(A[i])
            c[i]=cnt
        return c