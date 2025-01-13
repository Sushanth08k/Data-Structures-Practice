# 103. Binary Tree Zigzag Level Order Traversal
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr=[]
        if not root:
            return arr
        q=deque()
        q.append(root)
        left_right=True
        while q:
            size=len(q)
            row=[0]*size
            for i in range(size):
                node=q.popleft()
                index=i if left_right else (size-i-1)
                row[index]=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            left_right= not left_right
            arr.append(row)
        return arr