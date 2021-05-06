#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        sum=0
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    temp=0
                    if i>0 and grid[i-1][j]==1:
                        temp+=1
                    if i<m-1 and grid[i+1][j]==1:
                        temp+=1
                    if j>0 and grid[i][j-1]==1:
                        temp+=1
                    if j<n-1 and grid[i][j+1]==1:
                        temp+=1
                    sum+=(4-temp)
        return sum    
                    


# @lc code=end

