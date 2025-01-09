# 1408 String Matching in an Array
# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        l=[]
        for i in range(len(words)):
            m=words[i]
            c=0
            for j in range(len(words)):
                if m in words[j]:
                    c+=1
            if c>1:
                l.append(words[i])
        return l