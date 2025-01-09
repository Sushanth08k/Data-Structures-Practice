// 2185. Counting Words With a Given Prefix
// Input: words = ["pay","attention","practice","attend"], pref = "at"
// Output: 2
// Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".

class Solution {
    public int prefixCount(String[] words, String pref) {
        int n=pref.length();
        int cnt=0;
        for (int i=0;i<words.length;i++){
            if (words[i].length()>=n){
                System.out.println(words[i].substring(0,n));
                if (words[i].substring(0,n).equals(pref)){
                    cnt+=1;
                }
            }
        }
        return cnt;
    }
}