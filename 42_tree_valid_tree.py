# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, minVal,maxVal):
            if not root:
                return True
            
            left = valid(root.left,minVal, root.val)
            right = valid(root.right,root.val, maxVal)
            
            compareWithParent = root.val > minVal and root.val < maxVal
            
            
            
            return compareWithParent and left and right
       
        return valid(root, float("-inf"), float("inf"))
             