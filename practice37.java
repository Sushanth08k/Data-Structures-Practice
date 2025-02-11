//153. Find Minimum in Rotated Sorted Array
class Solution {
    public int findMin(int[] nums) {
        int low=0;
        int n=nums.length;
        int high =n-1;
        int ans=Integer.MAX_VALUE;
        while(low<=high){
            int mid=(low+high)/2;
            if (nums[low]<=nums[high]){
                ans=Math.min(ans,nums[low]);
                break;
            }
            if (nums[mid]>=nums[low]){
                ans=Math.min(ans,nums[low]);
                low=mid+1; 
            }
            else{
                ans=Math.min(ans,nums[mid]);
                high=mid-1;
            }
        }
        return ans;
    }
}