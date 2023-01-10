class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1,1,2,5]
        total = sum(dp)
        for i in range(4, n+1):
            val = total * 2 - (dp[i-1] + dp[i-2])
            dp.append(val)
            total += val
        print(dp)
        return dp[n] % (10**9 + 7)