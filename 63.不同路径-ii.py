#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if m==1 and n==1 and obstacleGrid[0][0]==0:
            return 1
        if m==1 and n==1 and obstacleGrid[0][0]==1:
            return 0
        dp=[[0 for _ in range(n)] for _ in range(m)]
        dp[0][0]=1-obstacleGrid[0][0]
        if m>1:
            for i in range(1,m):
                if obstacleGrid[i][0]==1:
                    dp[i][0]=0
                    continue
                dp[i][0]=dp[i-1][0]
        if n>1:
            for j in range(1,n):
                if obstacleGrid[0][j]==1:
                    dp[0][j]=0
                    continue
                dp[0][j]=dp[0][j-1]
        print(dp)
        if m==1:
            return dp[0][n-1]
        if n==1:
            return dp[m-1][0]
        for i in range(1,m):
            for j in range(1,n):
                print(i,j)
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                    continue
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[i][j]
# @lc code=end

