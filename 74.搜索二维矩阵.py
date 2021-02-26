#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        row_index=-2
        for i in range(m):
            if target<matrix[i][0]:
                row_index=i-1
                break
        if row_index==-2 and target not in matrix[m-1]:
            return False
        elif row_index==-2 and target in matrix[m-1]:
            return True
        if row_index<0:
            return False
        if target not in matrix[row_index]:
            return False
        else:
            return True
# @lc code=end

