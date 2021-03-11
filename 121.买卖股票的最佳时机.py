#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        start=prices[0]
        for i in range(1,len(prices)):
            if prices[i]>start:
                res=max(res,prices[i]-start)
            else:
                start=prices[i]
        return res
# @lc code=end

