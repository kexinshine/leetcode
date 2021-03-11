#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=[]
        dp.append(triangle[0])
        m=len(triangle)
        for i in range(1,m):
            temp=[dp[i-1][0]+triangle[i][0]]
            for j in range(1,i):
                temp.append(min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j])
            temp.append(dp[i-1][-1]+triangle[i][-1])
            dp.append(temp)
        return min(dp[-1])
# @lc code=end

