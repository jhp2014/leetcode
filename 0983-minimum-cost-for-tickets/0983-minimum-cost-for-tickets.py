class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366
        
        before = 0
        for day in days:

            for i in range(before, day):
                dp[i] = dp[before]
                
            ticket_7 = day - 7
            ticket_30 = day - 30
            if ticket_30 < 0:
                ticket_30 = 0
            if ticket_7 < 0:
                ticket_7 = 0
            dp[day] = min(costs[0] + dp[before], costs[1] + dp[ticket_7], costs[2] + dp[ticket_30])
            before = day
        return dp[days[-1]]
             