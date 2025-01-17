#260. Single Number III
# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice.
# Find the two elements that appear only once. You can return the answer in any order.
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans=[]
        nums.sort()
        i=0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                i+=2
            else:
                ans.append(nums[i])
                i+=1
        if len(ans)!=2:
            ans.append(nums[len(nums)-1])
        return ans