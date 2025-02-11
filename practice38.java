//2110. Number of Smooth Descent Periods of a Stock
// You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.
// A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.
// Return the number of smooth descent periods
// Input: prices = [3,2,1,4]
// Output: 7
// Explanation: There are 7 smooth descent periods:
// [3], [2], [1], [4], [3,2], [2,1], and [3,2,1]

class Solution {
    public long getDescentPeriods(int[] prices) {
        int n=prices.length;
        long cnt=0;
        long cur=1;
        for (int i=1;i<n;i++){
            if (prices[i]-prices[i-1]==-1){
                cur+=1;
            }
            else{
                cur=1;
            }
            cnt+=cur;
        }
        return cnt+1;
    }
}