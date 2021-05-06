#
# @lc app=leetcode.cn id=417 lang=python3
#
# [417] 太平洋大西洋水流问题
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        pos=[(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(x,y):
            if (x,y) in memo:
                return memo[(x,y)]
            visited[x][y]=1

            ans=0
            if x==0 or y==0:
                ans |= 2

            if x==m-1 or y==n-1:
                ans |= 1     
            
            for dx,dy in pos:
                xx,yy=x+dx,y+dy
                if 0<=xx<m and 0<=yy<n and heights[xx][yy]<=heights[x][y] and not visited[xx][yy]:
                    ans |= dfs(xx,yy)
            return ans            

        memo={}
        res=[]
        visited=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                visited=[[0]*n for _ in range(m)]
                ans = dfs(i,j)
                memo[(i,j)]=ans
                if ans==3:
                    res.append((i,j))                

        return res


        
        
        

        # @lc code=end

