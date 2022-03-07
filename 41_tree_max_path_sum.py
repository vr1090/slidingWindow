# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = []
        if not root:
            return 0
        
        result.append(root.val)
        
        
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
         
            maxLeft = max(left, 0)
            maxRight = max(right, 0)
            
            result[0] = max(result[0],root.val + maxLeft + maxRight)
            
            
            return root.val + max(maxLeft, maxRight)
        
        dfs(root)
        
        
        return result[0]
        