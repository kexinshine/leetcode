#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        mark=list()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    mark.append([i,j])
        for x in mark:
            for i in range(m):
                matrix[i][x[1]]=0
            for j in range(n):
                matrix[x[0]][j]=0

# @lc code=end

