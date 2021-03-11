#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def nums(list1):
            dp1=[0]
            start=list1[0]
            for i in range(1,len(list1)):
                if list1[i]>start:
                    dp1.append(max(dp1[i-1],list1[i]-start))
                else:
                    dp1.append(dp1[i-1])
                    start=list1[i]
            dp2=[0]
            list2=list(reversed(list1))
            start=list2[0]
            for i in range(1,len(list2)):
                if list2[i]<start:
                    dp2.append(max(dp2[i-1],-(list2[i]-start)))
                else:
                    dp2.append(dp2[i-1])
                    start=list2[i]
            return dp1[1:-1],dp2[1:-1]
        dp1,dp2=nums(prices)
        ans=0
        m=len(prices)
        if m==1:
            return 0
        if m==2:
            temp=prices[1]-prices[0]
            if temp>0:
                return temp
            else:
                return 0
        for i in range(m-2):
            ans=max(ans,dp2[-(i+1)]+dp1[i])
        return ans
# @lc code=end

