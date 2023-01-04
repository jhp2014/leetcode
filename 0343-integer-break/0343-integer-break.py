class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1]*(n+1)
        
        for i in range(3, n+1):
            temp = 0
            for j in range(1, i):
                temp = max(temp, (i-j) * dp[j], dp[i-j] * dp[j], (i-j) * j)
            dp[i] = temp
        return dp[n]