# 2381-Shifting Letters2
# You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. 
# For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.
# Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
# Output: "ace"
def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        s = list(s)
        shiftlist=[0]*(n+1)
        for start, end, direction in shifts:
            if direction==0:
                shiftlist[start]-=1
                shiftlist[end+1]+=1
            else:
                shiftlist[start]+=1
                shiftlist[end+1]-=1
        currentshift=0
        for i in range(n):
            currentshift+=shiftlist[i]
            netshift=(currentshift%26+26)%26
            s[i]=chr(((ord(s[i])-ord('a')+netshift)%26)+ord('a'))
        return "".join(s)