# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            if left < 0:
                return -1
            right = dfs(root.right)
            if right < 0 or abs(left-right) > 1:
                return -1

            return max(right, left) + 1

        return dfs(root) >= 0