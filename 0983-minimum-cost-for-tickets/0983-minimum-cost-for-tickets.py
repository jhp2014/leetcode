class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366
        
        before = 0
        for day in days:

            for i in range(before+1, day):
                dp[i] = dp[i-1]
            dp[day] = min(costs[0] + dp[before], costs[1] + dp[max(0, day - 7)], costs[2] + dp[max(0, day - 30)])
            
            before = day
        return dp[days[-1]]
             