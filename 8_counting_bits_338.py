class Solution:
    def countBits(self, n: int) -> List[int]:
        offset = 1
        dp = [0] * (n+1)
        dp[0] = 0
        
        for i in range(1, n+1):
            
            if offset * 2 == i:
                offset = i
            
            dp[i] = 1+ dp[i-offset]
        
        
        return dp
        