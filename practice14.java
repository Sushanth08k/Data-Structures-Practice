class Solution {
    public int maxScore(String s) {
        int zero=0;
        int one=0;
        for(int i=0;i<s.length();i++){
            if (s.charAt(i)=='0'){
                zero++;
            }
            else{
                one++;
            }
        }
        int left=0;
        int right=0;
        int score =-1;
        for(int i=0;i<s.length()-1;i++){
            if (s.charAt(i)=='0'){
                left++;
                right=one;
            }
            else{
                one--;
                right=one;
            }
            score=Math.max(score,left+right);
        }
        return score;
    }
}