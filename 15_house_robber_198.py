class Solution:
    def rob(self, nums: List[int]) -> int:
        dp= [0] * (len(nums)+ 2)
        
        for i in range(2, len(nums)+ 2):
            maxNum = 0
            for j in range( i-2, -1,-1):
                maxNum = max(maxNum, dp[j])
            dp[i] = nums[i-2] + maxNum
        
        return max(dp)
        