class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * n
        dp[0] = arr[0]

        for i in range(1, n):
            
            for j in range(k):
                if i-j > 0:
                    val = max(arr[i-j:i+1]) * (j+1) + dp[i-(j+1)]
                    dp[i] = max(val, dp[i])
                else:
                    val = max(arr[0:i+1]) * (i+1)
                    dp[i] = max(val, dp[i])

        
        return dp[n-1]
                    
                    
