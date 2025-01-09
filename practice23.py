#124. Binary Tree Maximum Path Sum
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def path(node,pathsum):
            if node is None:
                return 0
            left_sum=max(0,path(node.left,pathsum))
            right_sum=max(0,path(node.right,pathsum))
            pathsum[0]=max(pathsum[0],left_sum+right_sum+node.val)
            return node.val+max(left_sum,right_sum)
        pathsum=[float('-inf')]
        path(root,pathsum)
        return pathsum[0]