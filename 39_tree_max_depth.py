# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def cekDepth(node,depth):
            if node is None:
                return depth
            else:
                return max(cekDepth(node.left, depth+1), cekDepth(node.right, depth+1))
        
        return cekDepth(root,0)
        