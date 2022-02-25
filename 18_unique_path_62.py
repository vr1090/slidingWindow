class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp= [[0] *n for i in range(m)]
        
        for i in range(m):
            dp[i][0]=1
            
        for i in range(n):
            dp[0][i]=1
            
        for i in range(1, m):
            for j in range(1,n):
                left = dp[i][j-1] if j-1 >= 0 else 0
                top = dp[i-1][j] if i-1 >= 0 else 0
                dp[i][j]=left + top
            
        return dp[m-1][n-1]