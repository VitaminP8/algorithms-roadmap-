# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            rightSide = None

            for i in range(len(q)):
                temp = q.popleft()
                if temp:
                    rightSide = temp
                    q.append(temp.left)
                    q.append(temp.right)

            if rightSide:
                res.append(rightSide.val)

        return res

