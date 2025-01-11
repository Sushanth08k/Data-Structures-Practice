# 1400. Construct K Palindrome Strings
# Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise
# Input: s = "annabelle", k = 2
# Output: true
# Explanation: You can construct two palindromes using all characters in s.
# Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s)<k:
            return False
        hash1=[0]*26
        for i in range(len(s)):
            ind=ord(s[i])-ord('a')
            hash1[ind]+=1
        cnt=0
        for i in hash1:
            if i%2!=0:
                cnt+=1
        if cnt>k:
            return False
        return True