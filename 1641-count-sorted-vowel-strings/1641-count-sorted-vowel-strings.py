class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(5)]
        
        for i in range(5):
            dp[i][1] = i+1
        for i in range(1, n+1):
            dp[0][i] = 1
        
        for i in range(1, 5):
            for j in range(2, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[4][n]
            