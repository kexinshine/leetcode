#
# @lc app=leetcode.cn id=214 lang=python3
#
# [214] 最短回文串
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(set(s))==1:
            return s
        if not s:
            return s
        n=len(s)
        dp=[[True]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                dp[i][j]=(s[i]==s[j] and dp[i+1][j-1])
        temp=dp[0]
        for i in range(n):
            if not temp[i]:
                continue
            max_index=i
        if max_index==n-1:
            return s
        ans=s
        for j in range(max_index+1,n):
            ans=s[j]+ans
        return ans
        
# @lc code=end

