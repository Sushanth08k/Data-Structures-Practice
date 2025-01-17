#2425. Bitwise XOR of All Pairings
# Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
# Output: 13
# Explanation:
# A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
# The bitwise XOR of all these numbers is 13, so we return 13.

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        c1 = len(nums1)
        c2 = len(nums2)
        x1 = 0
        x2 = 0
        if c1 % 2 != 0:
            for i in nums2:
                x2 ^= i
        if c2 % 2 != 0:
            for i in nums1:
                x1 ^= i
        return x1 ^ x2