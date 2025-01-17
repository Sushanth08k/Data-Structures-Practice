//137. Single Number II
//Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
// Input: nums = [2,2,3,2]
// Output: 3
class Solution {
    public int singleNumber(int[] nums) {
        Arrays.sort(nums);
        for (int i=1;i<nums.length;i=i+3){
            if (nums[i-1]!=nums[i]){
                return nums[i-1];
            }
        }
        return nums[nums.length-1];
    }
}