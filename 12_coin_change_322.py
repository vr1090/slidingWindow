class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [0] * (amount+1)
        
        for i in range(1,amount+1):
            minimum = 100000
            for c in coins:
                if( i-c >=0):
                    minimum = min(minimum, 1+dp[i-c])
            
            dp[i] = minimum
        
        return dp[amount] if dp[amount] < 100000 else -1