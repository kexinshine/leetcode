#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        if m<n:
            return 0
        dp=[[0 for j in range(n)] for i in range(m)]
        if s[0]==t[0]:
            dp[0][0]=1
        for i in range(1,m):
            if s[i]==t[0]:
                dp[i][0]=dp[i-1][0]+1
            else:
                dp[i][0]=dp[i-1][0]
        for i in range(1,n):
            for j in range(1,m):
                if s[j]==t[i]:
                    dp[j][i]=dp[j-1][i-1]+dp[j-1][i]
                else:
                    dp[j][i]=dp[j-1][i]
        return dp[m-1][n-1]
# @lc code=end

