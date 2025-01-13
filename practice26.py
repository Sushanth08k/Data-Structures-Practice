# 2116. Check if a Parentheses String Can Be Valid
# Input: s = "))()))", locked = "010100"
# Output: true
# Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
# We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n=len(s)
        if n%2!=0:
            return False
        bal=0
        for i in range(len(s)):
            if (locked[i]=='0') or (s[i]=='('):
                bal+=1
            else:
                bal-=1
            if bal<0:
                return False
        balrev=0
        for i in range(n-1,-1,-1):
            if locked[i]=='0' or s[i]==')':
                balrev+=1
            else:
                balrev-=1
            if balrev<0:
                return False
        return True