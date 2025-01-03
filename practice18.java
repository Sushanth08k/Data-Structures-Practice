// 2270 - Number of ways to split Array
// The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
// There is at least one element to the right of i. That is, 0 <= i < n - 1.
// Return the number of valid splits in nums.
// Input: nums = [10,4,-8,7]
// Output: 2
class Solution {
    public int waysToSplitArray(int[] nums) {
        long[] prefix_sum=new long[nums.length];
        long sum=0;
        for(int i=0;i<nums.length;i++){
            sum+=nums[i];
            prefix_sum[i]=sum;
        }
        
        int count=0;
        for(int i=0;i<nums.length-1;i++){
            if ((prefix_sum[nums.length-1]-prefix_sum[i])<=prefix_sum[i]){
                count++;
            }
        }   System.out.println(count);
        return count;

    }
}