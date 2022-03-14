# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        cur = root
        n = 0
        # ga finish, sampai ada yg null
        while cur and stack:
            # loop terus ke kiri
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # mulai process
            # ini dijamin yg paling kiri
            # pop it
            cur = stack.pop()
            n = n + 1

            if n == k:
                return cur.val
            
            cur = cur.right
