#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        def maxmal(dp):
            max_mal=0
            temp=[]
            for i in range(len(dp)):
                if dp[i]==0:
                    if temp:

                        temp=[]
                    continue
                temp.append(dp[i])
            return max_mal
        m=len(matrix)
        n=len(matrix[0])
        dp=[0]*n
        for i in range(n):
            if matrix[0][i]=='1':
                dp[i]=1
            else:
                dp[i]=0
        max_mal=maxmal(dp)
        for i in range(1,m):
            for j in range(n):
                if matrix[i][j]=='1':
                    dp[j]=dp[j]+1
                else:
                    dp[j]=0
            max_mal=max(max_mal,maxmal(dp))
        return max_mal
# @lc code=end

