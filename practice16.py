##2559 Count Vowels Strings in Ranges
# Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.
# Return an array ans of size queries.length, where ans[i] is the answer to the ith query.
# Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
# Output: [2,3,0]

def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels={'a', 'e', 'i', 'o','u'}
        prefix_sum=[0]*len(words)
        sum=0
        for i in range(len(words)):
            if (words[i][0] in vowels) and (words[i][-1]in vowels):
                sum+=1
            prefix_sum[i]=sum
        print(prefix_sum)
        l=[]
        for i in range(len(queries)):
            if queries[i][0]!=0:
                l.append(prefix_sum[queries[i][1]]-prefix_sum[queries[i][0]-1])
            else:
                l.append(prefix_sum[queries[i][1]])
        return l