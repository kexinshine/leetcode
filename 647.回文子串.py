#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        dp=[[True]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                dp[i][j]=(s[i]==s[j] and dp[i+1][j-1])
        ans=list()
        for i in range(n):
            for j in range(n):
                if dp[i][j] and s[i:j+1]:
                    ans.append(s[i:j+1])
        return len(ans)
# @lc code=end

