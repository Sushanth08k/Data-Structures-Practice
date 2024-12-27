class Solution {
    public int maxScoreSightseeingPair(int[] values) {
        int cur=0;
        int maxval=0;
        int n=values.length;
        for(int i=1;i<n;i++){
            cur=Math.max(cur,values[i-1]+i-1);
            maxval=Math.max(maxval,cur+values[i]-i);
        }
        return maxval;
    }
}