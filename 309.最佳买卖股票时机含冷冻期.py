#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n=len(prices)
        dp=[[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]
        for i in range(1,n):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]-prices[i])
            dp[i][1]=max(dp[i-1][1],dp[i-1][2])
            dp[i][2]=dp[i][0]+prices[i]
        return max(dp[n-1][1],dp[n-1][2])

# @lc code=end

