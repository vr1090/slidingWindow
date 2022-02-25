class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) -1
        maxLen = len(nums) -1
        
        for j in range( maxLen, -1,  -1) :
            if  j + nums[j]  >= goal:
                goal = j
        
        return goal == 0