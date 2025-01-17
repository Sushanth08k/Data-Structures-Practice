#3223. Minimum Length of String After Operations
# Input: s = "abaacbcbb"
# Output: 5
# Explanation:
# We do the following operations:
# Choose index 2, then remove the characters at indices 0 and 3. The resulting string is s = "bacbcbb".
# Choose index 3, then remove the characters at indices 0 and 5. The resulting string is s = "acbcb".
class Solution:
    def minimumLength(self, s: str) -> int:
        l=0
        hash1=[0]*26
        for i in range(len(s)):
            hash1[ord(s[i])-ord('a')]+=1
        for i in hash1:
            if i==0:
                continue
            elif i%2==0:
                l+=2
            else:
                l+=1
        return l