// 1769. Minimum Number of Operations to Move All Balls to Each Box
// Input: boxes = "110"
// Output: [1,1,3]
// Explanation: The answer for each box is as follows:
// 1) First box: you will have to move one ball from the second box to the first box in one operation.
// 2) Second box: you will have to move one ball from the first box to the second box in one operation.
// 3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
class Solution {
    public int[] minOperations(String boxes) {
        int[] res =new int[boxes.length()];
        int fps=0;
        int count=0;
        for(int i=0;i<boxes.length();i++){
            res[i]+=fps;
            count+= boxes.charAt(i)=='1'?1:0;
            fps+=count;
        }
        int fps1=0;
        int count1=0;
        for(int i=boxes.length()-1;i>=0;i--){
            res[i]+=fps1;
            count1+= boxes.charAt(i)=='1'?1:0;
            fps1+=count1;
        }
        return res;
    }
}